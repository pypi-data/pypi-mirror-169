import os
import logging
from typing import AnyStr, cast, Optional, Tuple

from azure.core.exceptions import ServiceRequestError, ResourceNotFoundError
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

logger = logging.getLogger(__name__)
_azure_credential = DefaultAzureCredential(
    exclude_cli_credential=os.environ.get("AZURE_EXCLUDE_CLI_CREDENTIAL", False),
    exclude_environment_credential=os.environ.get("AZURE_EXCLUDE_ENVIRONMENT_CREDENTIAL", False),
    exclude_managed_identity_credential=os.environ.get("AZURE_EXCLUDE_MANAGED_IDENTITY_CREDENTIAL", False),
    exclude_powershell_credential=os.environ.get("AZURE_EXCLUDE_POWERSHELL_CREDENTIAL", False),
    exclude_visual_studio_code_credential=os.environ.get("AZURE_VISUAL_STUDIO_CODE_CREDENTIAL", True),
    exclude_shared_token_cache_credential=os.environ.get("AZURE_SHARED_TOKEN_CACHE_CREDENTIAL", False),
    exclude_interactive_browser_credential=os.environ.get("AZURE_INTERACTIVE_BROWSER_CREDENTIAL", True),
)


def inject_secret_from_key_vault(obj, field: str):
    """
    Replace attribute of an object by secret from Azure Key Vault if attribute matches secret specification
    :param obj: object to target
    :param field: field to target
    :return:
    """
    secret = secret_from_key_vault(field, getattr(obj, field))
    if secret is None:
        return
    setattr(obj, field, secret)


def replace_secret_from_key_vault(field: str, value: str) -> str:
    """
    Replace value by secret from Azure Key Vault if value matches secret specification
    :param field: name of field
    :param value: value to replace
    :return: secret if value matches secret specification, otherwise the input value
    """
    secret = secret_from_key_vault(field, value)
    if secret is None:
        return value
    return secret


def parse_secret_def(value: Optional[str]) -> Optional[Tuple[str, str]]:
    """
    Parse secret definition as per secret specification 'KEY_VAULT_NAME|SECRET_NAME'
    :param value: value to parse
    :return: tuple of (KEY_VAULT_NAME, SECRET_NAME) if the value matches the secret specification, otherwise None
    """
    if value is None:
        return None
    if not isinstance(value, str):
        return None
    parts = value.split("|")
    if len(parts) != 2:
        return None
    return parts[0], parts[1]


def secret_from_key_vault(field: str, value: Optional[str]) -> Optional[str]:
    """
    Load secret from Azure key vault
    :param field: name of field
    :param value: secret specification in the form 'KEY_VAULT_NAME|SECRET_NAME'
    :return: secret if the value matches the secret specification, otherwise None
    """
    parts = parse_secret_def(value)
    if parts is None:
        return None
    # Read secret from Azure key vault.
    try:
        vault_url = f"https://{parts[0]}.vault.azure.net"
        client = SecretClient(vault_url=vault_url, credential=_azure_credential)
        return client.get_secret(parts[1]).value
    except ServiceRequestError:
        logger.warning(
            f"Value of [{field}] matches secret specification, but the key vault was not found."
        )
        return None
    except ResourceNotFoundError:
        logger.warning(
            f"Value of [{field}] matches secret specification, but the secret was not found."
        )
        return None


def set_azure_loglevel(loglevel: int = logging.WARNING) -> logging.Logger:
    """Sets the log level of the azure loggers. Used to mute the very verbose
    azure.core.pipeline.policies.http_logging_policy logger.

    :param loglevel: logging level, e.g. logging.WARNING
    :return: logging.Logger for the azure logger."""
    az_logger = logging.getLogger("azure.core.pipeline.policies.http_logging_policy")
    az_logger.setLevel(loglevel)
    return az_logger


def raise_if_read_only(message: str = "Operation not permitted. Container is read only."):
    """Decorate *func* to raise IOError with *message*
    if the first argument to the function has a truthy field args[0].read_only."""

    def decorator(func):
        def wrapper(*args, **kwargs):
            if len(args) > 0:
                if getattr(args[0], "read_only", False):
                    raise IOError(message)
            return func(*args, **kwargs)

        return wrapper

    return decorator


def bytes_to_mode(value: bytes, mode: str) -> AnyStr:
    if "b" not in mode:
        output = cast(AnyStr, value.decode())
    else:
        output = cast(AnyStr, value)
    return output
