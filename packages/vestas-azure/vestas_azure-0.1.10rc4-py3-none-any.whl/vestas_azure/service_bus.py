import logging

from typing import Callable, Optional
from azure.servicebus import AutoLockRenewer, ServiceBusClient, ServiceBusMessage
from vestas_azure import settings, get_json_log_formatter


class AzureServiceBusLogHandler(logging.StreamHandler):
    """
    Log handler that routes logs to (a topic/subscription in) Azure Service Bus.
    """

    def __init__(
        self,
        topic_name: str,
        connection_string: Optional[str] = None,
        formatter: Optional[logging.Formatter] = None,
    ):
        logging.StreamHandler.__init__(self)
        self.topic_name = topic_name
        self.connection_string = _load_connection_string(connection_string)
        self.formatter = formatter if formatter is not None else get_json_log_formatter()

    def emit(self, record):
        servicebus_client = ServiceBusClient.from_connection_string(self.connection_string)
        with servicebus_client:
            sender = servicebus_client.get_topic_sender(topic_name=self.topic_name)
            with sender:
                message = ServiceBusMessage(self.format(record))
                sender.send_messages(message)


class AzureServiceBusLogReceiver:
    """
    Small class for creating a log receiver service, typically used to route logs elsewhere.
    """

    def __init__(
        self, topic_name: str, subscription_name: str, connection_string: Optional[str] = None
    ):
        self.topic_name = topic_name
        self.subscription_name = subscription_name
        self.connection_string = _load_connection_string(connection_string)

    def run(self, message_handler: Callable):
        """
        Run the log receiver forever, i.e. this call is blocking. Call it to start the receiver service
        :param message_handler: function that handles the message
        :return: None
        """
        servicebus_client = ServiceBusClient.from_connection_string(self.connection_string)
        with servicebus_client:
            receiver = servicebus_client.get_subscription_receiver(
                topic_name=self.topic_name, subscription_name=self.subscription_name
            )
            with receiver:
                for msg in receiver:
                    message_handler(msg)
                    receiver.complete_message(msg)


def bind_default_auto_lock_renewer(auto_lock_renewer: AutoLockRenewer):
    """
    Per default, auto lock renewal is disabled. Use this function to enable auto lock renewable (by default), useful
    e.g. for cases when you do not control the instantiation of the ServiceBusClient object.
    :param auto_lock_renewer: an AutoLockRenewer object
    :return: None
    """

    original = ServiceBusClient.get_queue_receiver

    def patch(*args, **kwargs):
        if "auto_lock_renewer" not in kwargs:
            kwargs["auto_lock_renewer"] = auto_lock_renewer
        return original(*args, **kwargs)

    ServiceBusClient.get_queue_receiver = patch  # type: ignore


def _load_connection_string(connection_string: Optional[str]) -> str:
    if connection_string is not None:
        return connection_string
    if settings.SERVICE_BUS_CONNECTION_STRING is not None:
        return settings.SERVICE_BUS_CONNECTION_STRING
    raise ValueError("SERVICE_BUS_CONNECTION_STRING not set")
