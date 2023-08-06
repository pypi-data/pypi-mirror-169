import os
import sys
from typing import Optional, Callable, List, TypeVar, Type

from dotenv import load_dotenv
from dotenv.main import _walk_to_root
from pydantic import BaseSettings, Field
from vestas_azure.utils import inject_secret_from_key_vault

# region Generic config logic

T = TypeVar("T", bound=BaseSettings)


class AzureConfig:
    """
    An object used for loading/parsing settings. Supports loading of settings from secrets stored in Azure key vaults
    using the syntax 'KEY_VAULT_NAME|SECRET_NAME'.
    """

    def __init__(self, settings_type: Type[T], post_parse: Optional[Callable[[T], T]] = None):
        self._settings_type = settings_type
        self._post_parse = post_parse
        self.settings = self.parse_settings()

    def parse_settings(self):
        """
        Parse settings from environment variables.
        """
        _settings = self._settings_type()
        for field in _extract_settings_fields(_settings):
            inject_secret_from_key_vault(_settings, field)
        if self._post_parse:
            _settings = self._post_parse(_settings)
        return _settings

    def reload_settings(self):
        """
        Reload settings from environment variables in-place.
        """
        _settings = self.parse_settings()
        for field in _extract_settings_fields(_settings):
            setattr(self.settings, field, getattr(_settings, field))

    def load_settings(self, dotenv_path: Optional[str] = None, **kwargs):
        """
        Load settings using dotenv, i.e. first load the provided file, then reload settings.
        """
        if dotenv_path is None:
            protected_load_dotenv()
        else:
            load_dotenv(dotenv_path, **kwargs)
        self.reload_settings()


def _extract_settings_fields(obj: T) -> List[str]:
    """
    Small utility function that extracts the available settings as a list of strings.
    :param obj: settings object
    :return: list of settings
    """
    return list(set(dir(obj)).difference(set(dir(BaseSettings()) + ["__annotations__"])))


def protected_load_dotenv():
    """
    Small wrapper around load_dotenv that supports skipping loading (via the 'SKIP_LOAD_DOTENV' environment variable).
    :return:
    """
    if os.getenv("SKIP_LOAD_DOTENV") is not None:
        return
    for dp in [os.path.dirname(sys.argv[0]), os.getcwd()]:
        if not os.path.exists(dp):
            continue
        for dirname in _walk_to_root(dp):
            check_path = os.path.join(dirname, ".env")
            if os.path.isfile(check_path):
                load_dotenv(check_path)


# endregion

# region Library specific logic (can be used as a template for other libraries)


class VazSettings(BaseSettings):
    TENANT_ID: Optional[str]
    CLIENT_ID: Optional[str]
    CLIENT_SECRET: Optional[str]
    BLOB_STORAGE_CONTAINER: Optional[str]
    BLOB_STORAGE_ACCOUNT_NAME: Optional[str]
    BLOB_STORAGE_ACCOUNT_KEY: Optional[str]
    SERVICE_BUS_CONNECTION_STRING: Optional[str]

    class Config:
        env_prefix = "VAZ_"


def _set_env(key, value):
    if value is None or os.getenv(key) is not None:
        return
    os.environ[key] = value


def _handle_adlfs_env(vs: VazSettings) -> VazSettings:
    _set_env("AZURE_TENANT_ID", vs.TENANT_ID)
    _set_env("AZURE_CLIENT_ID", vs.CLIENT_ID)
    _set_env("AZURE_CLIENT_SECRET", vs.CLIENT_SECRET)
    _set_env("AZURE_STORAGE_CONTAINER", vs.BLOB_STORAGE_CONTAINER)
    _set_env("AZURE_STORAGE_ACCOUNT_KEY", vs.BLOB_STORAGE_ACCOUNT_KEY)
    _set_env("AZURE_STORAGE_ACCOUNT_NAME", vs.BLOB_STORAGE_ACCOUNT_NAME)
    return vs


protected_load_dotenv()  # load env variables
cfg = AzureConfig(VazSettings, post_parse=_handle_adlfs_env)  # parse settings
settings: VazSettings = cfg.settings  # make available as module level 'settings' attribute

# endregion
