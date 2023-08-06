import datetime
import os
import logging
from jsonformatter import JsonFormatter
from collections import OrderedDict
from typing import Optional, Dict, Callable, List, Tuple


def set_azure_loglevel(loglevel: int = logging.WARNING) -> logging.Logger:
    """Sets the log level of the azure loggers. Used to mute the very verbose
    azure.core.pipeline.policies.http_logging_policy logger.

    :param loglevel: logging level, e.g. logging.WARNING
    :return: logging.Logger for the azure logger."""
    logger = logging.getLogger("azure.core.pipeline.policies.http_logging_policy")
    logger.setLevel(loglevel)
    return logger


def set_uamqp_loglevel(loglevel: int = logging.WARNING) -> logging.Logger:
    """Sets the log level of the uamqp loggers. Used to mute the very verbose uamqp.connection, uamqp.c_uamqp, and
    uamqp.receiver loggers.

    :param loglevel: logging level, e.g. logging.WARNING
    :return: logging.Logger for the uamqp logger."""
    logger = logging.getLogger("uamqp")
    logger.setLevel(loglevel)
    return logger


# region General log utils. Should they be here?


def detect_if_running_in_kubernetes() -> bool:
    return bool(os.environ.get("KUBERNETES_PORT", default=False))


def get_json_log_file_name() -> str:
    filename = os.environ.get("JSON_LOG_FILE", default="gemini_json_logs.txt")
    return filename


def configure_logging(
    log_level: Optional[int] = None,
    mute_uamqp_logger: bool = True,
    mute_azure_logger: bool = True,
    mute_uvicorn_and_gunicorn_logger: bool = True,
    extra_handlers: Optional[List[logging.Handler]] = None,
    k8s_formatter: Optional[logging.Formatter] = None,
) -> None:
    """Used to configure the logger to produce sane output
    :param log_level: integer logging level, e.g. logging.INFO
    :param mute_uamqp_logger: default is to mute the very verbose uamqp loggers
    :param mute_azure_logger: default is to mute the very verbose azure http logger
    :param mute_uvicorn_and_gunicorn_logger: default is to mute uvicorn and gunicorn loggers
    :param extra_handlers: list of handlers to attach, defaults to a stream handler
    :param k8s_formatter: format specification for k8s logger (optional, defaults to json log formatter)
    :return: None"""
    log_level = log_level if log_level is not None else get_log_level()
    sh = logging.StreamHandler()
    sh.setFormatter(get_human_readable_log_formatter())
    handlers: List[logging.Handler] = [sh]
    if extra_handlers is not None:
        handlers += extra_handlers
    if detect_if_running_in_kubernetes():
        k8s_formatter = k8s_formatter if k8s_formatter is not None else get_json_log_formatter()
        fh = logging.FileHandler(get_json_log_file_name(), mode="a")
        fh.setFormatter(k8s_formatter)
        handlers.append(fh)
    logging.basicConfig(level=log_level, force=True, handlers=handlers)
    if mute_uvicorn_and_gunicorn_logger:
        disable_uvicorn_and_gunicorn_loggers()
    if mute_azure_logger:
        set_azure_loglevel()
    if mute_uamqp_logger:
        set_uamqp_loglevel()


def add_logging_level(
    level_name: str, level_num: int, method_name: Optional[str] = None, raise_error=True
):
    """
    Comprehensively adds a new logging level to the `logging` module and the
    currently configured logging class.

    `level_name` becomes an attribute of the `logging` module with the value
    `level_num`. `method_name` becomes a convenience method for both `logging`
    itself and the class returned by `logging.getLoggerClass()` (usually just
    `logging.Logger`). If `method_name` is not specified, `level_name.lower()` is
    used.

    To avoid accidental clobberings of existing attributes, this method will
    raise an `AttributeError` if the level name is already an attribute of the
    `logging` module or if the method name is already present

    Example
    -------
    >>> addLoggingLevel('TRACE', logging.DEBUG - 5)
    >>> logging.getLogger(__name__).setLevel("TRACE")
    >>> logging.getLogger(__name__).trace('that worked')
    >>> logging.trace('so did this')
    >>> logging.TRACE
    5
    """
    level_name = level_name.upper()
    # ### Copied from
    # ### https://stackoverflow.com/a/35804945
    if not method_name:
        method_name = level_name.lower()
    error_msg = None
    if hasattr(logging, level_name):
        error_msg = "{} already defined in logging module".format(level_name)
    if hasattr(logging, method_name):
        error_msg = "{} already defined in logging module".format(method_name)
    if hasattr(logging.getLoggerClass(), method_name):
        error_msg = "{} already defined in logger class".format(method_name)
    if error_msg is not None:
        if raise_error:
            raise AttributeError(error_msg)
        else:
            logging.getLogger(__name__).warning(error_msg)

    # This method was inspired by the answers to Stack Overflow post
    # http://stackoverflow.com/q/2183233/2988730, especially
    # http://stackoverflow.com/a/13638084/2988730
    def logForLevel(self, message, *args, **kwargs):
        if self.isEnabledFor(level_num):
            # HJVKI: it is NOT an error that the args below does not have an
            # asterix!
            self._log(level_num, message, args, **kwargs)

    def logToRoot(message, *args, **kwargs):
        logging.log(level_num, message, *args, **kwargs)

    logging.addLevelName(level_num, level_name)
    setattr(logging, level_name, level_num)
    setattr(logging.getLoggerClass(), method_name, logForLevel)
    setattr(logging, method_name, logToRoot)


def disable_uvicorn_and_gunicorn_loggers():
    for name in [
        "gunicorn",
        "gunicorn.access",
        "gunicorn.error",
        "uvicorn",
        "uvicorn.access",
        "uvicorn.error",
    ]:
        logging.getLogger(name).handlers = []
        logging.getLogger(name).setLevel(get_log_level())


def get_json_log_formatter(
    record_custom_format: List[Tuple[str, str]] = None,
    record_custom_attrs: Dict[str, Callable] = None,
) -> logging.Formatter:
    _record_custom_attrs = {
        "utctime-isoformat": lambda: datetime.datetime.utcnow().isoformat(),
    }
    if record_custom_attrs:
        _record_custom_attrs.update(record_custom_attrs)
    _record_custom_format = OrderedDict(
        [
            ("name", "name"),
            ("level", "levelname"),
            ("pathname", "pathname"),
            ("filename", "filename"),
            ("module", "module"),
            ("lineno", "lineno"),
            ("function_name", "funcName"),
            ("timestamp", "utctime-isoformat"),
            ("msecs", "msecs"),
            ("message", "message"),
        ]
        + (record_custom_format if record_custom_format is not None else [])
    )
    return JsonFormatter(
        _record_custom_format,
        ensure_ascii=True,
        mix_extra=True,
        mix_extra_position="tail",
        record_custom_attrs=_record_custom_attrs,
    )


def get_human_readable_log_formatter() -> logging.Formatter:
    log_format = "%(asctime)s %(name)s %(levelname)s -- %(message)s"
    formatter = logging.Formatter(log_format)
    return formatter


def get_log_level() -> int:
    loglevel_environ = os.getenv("LOGLEVEL", default="INFO")
    loglevel_int = logging.getLevelName(loglevel_environ)
    if type(loglevel_int) == int:
        return loglevel_int
    else:
        return logging.INFO


class SingleLevelFilter(logging.Filter):
    def __init__(self, level):
        self.level = level

    def filter(self, log_record):
        return log_record.levelno == self.level


# endregion
