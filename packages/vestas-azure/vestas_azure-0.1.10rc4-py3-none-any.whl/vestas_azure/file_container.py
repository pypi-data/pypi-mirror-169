import logging
import os
import shutil as sh

from typing import List, Optional, Any, Union, AnyStr, Iterable, IO, cast, Dict
from azure.core.exceptions import HttpResponseError
from azure.storage.blob import ContainerClient
from pydantic import Field, BaseModel
from vestas_azure import get_container_client
from vestas_azure.utils import raise_if_read_only, bytes_to_mode, replace_secret_from_key_vault

logger = logging.getLogger(__name__)


class FileContainer:
    """
    Interface definition for file containers.
    """

    def read(self, key: str, namespace: Optional[List[str]] = None, mode: str = "rb") -> AnyStr:
        """Read object data from container"""

    def write(
        self, key: str, value: Any, namespace: Optional[List[str]] = None, mode: str = "rb"
    ):
        """Write object data to container"""

    def get(
        self,
        key: str,
        namespace: Optional[List[str]] = None,
        exist_ok: bool = True,
        missing_ok: bool = True,
    ) -> str:
        """Get object path in container"""
        # If key has been read from Excel and was blank this evaluates to nan which fails.
        # Check for this:
        if not type(key) == str:
            raise ValueError(f"No filename specified: (key={key} in namespace={namespace})")
        if not exist_ok and self.has(key, namespace):
            raise FileExistsError(f"Key [{key}] already exists in [{namespace}].")
        if not missing_ok and not self.has(key, namespace):
            current = ",".join(self.list(namespace))
            raise FileNotFoundError(
                f"Key [{key}] was not found in [{namespace}]. Current keys are [{current}]."
            )
        return self._get(key, namespace)

    def _get(self, key: str, namespace: Optional[List[str]] = None) -> str:
        """Implementation of how to get object path in container"""

    def has(self, key: str, namespace: Optional[List[str]] = None) -> bool:
        """Check if keys is in store"""

    def list(self, namespace: Optional[List[str]] = None) -> List[str]:
        """List keys in namespace"""

    def remove(self, key: Optional[str] = None, namespace: Optional[List[str]] = None):
        """Remove keys and/or namespaces"""

    def describe(self) -> str:
        """Container description"""

    def get_options(self) -> Dict[str, str]:
        """Optionally  expose options for underlying transports"""


class DiskContainer(BaseModel, FileContainer):
    """
    Disk based implementation of FileContainer.
    """

    type: str = Field("DiskContainer", const=True)

    wd: str = Field(default=".", description="Base")
    base_namespace: Optional[List[str]] = None
    create_dirs: bool = True
    read_only: bool = False

    def read(self, key: str, namespace: Optional[List[str]] = None, mode: str = "rb") -> AnyStr:
        with open(self.get(key, namespace), mode) as f:
            return f.read()

    @raise_if_read_only()
    def write(
        self, key: str, value: AnyStr, namespace: Optional[List[str]] = None, mode: str = "wb"
    ):
        with open(self.get(key, namespace), mode) as f:
            f.write(value)

    def _get(self, key: str, namespace: Optional[List[str]] = None) -> str:
        return os.path.join(self._get_dir(namespace), key)

    def has(self, key: str, namespace: Optional[List[str]] = None) -> bool:
        return os.path.isfile(self._get(key, namespace))

    def list(self, namespace: Optional[List[str]] = None) -> List[str]:
        return os.listdir(self._get_dir(namespace))

    @raise_if_read_only()
    def remove(self, key: Optional[str] = None, namespace: Optional[List[str]] = None):
        if key is None:
            return sh.rmtree(self._get_dir(namespace))
        os.remove(self.get(key, namespace))

    def describe(self) -> str:
        return f"{self.__class__.__name__}@{self.wd}"

    def _get_dir(self, namespace: Optional[List[str]] = None) -> str:
        namespace = namespace if namespace is not None else []
        if self.base_namespace:
            namespace = self.base_namespace + namespace
        dir_path = os.path.join(self.wd, *namespace)
        if self.create_dirs:
            os.makedirs(dir_path, exist_ok=True)
        return dir_path

    @staticmethod
    def _ensure_dirs_exit(
        dir_path: str, fn: Optional[str] = None, sd: Optional[str] = None, create: bool = True
    ) -> str:
        dir_path = os.path.join(dir_path, sd) if sd else dir_path
        if create:
            os.makedirs(dir_path, exist_ok=True)
        return dir_path if not fn else os.path.join(dir_path, fn)

    def get_options(self) -> Dict[str, str]:
        return {}


class DictContainer(BaseModel, FileContainer):
    """
    In memory implementation of FileContainer using a dictionary as backend.
    """

    type: str = Field("DictContainer", const=True)

    base_namespace: Optional[List[str]] = None
    read_only: bool = False
    data: Dict[str, Any] = {}

    def read(
        self, key: str, namespace: Optional[List[str]] = None, mode: Optional[str] = None
    ) -> Any:
        return self.data[self.get(key, namespace)]

    @raise_if_read_only()
    def write(
        self,
        key: str,
        value: Any,
        namespace: Optional[List[str]] = None,
        mode: Optional[str] = None,
    ):
        self.data[self.get(key, namespace)] = value

    def _get(self, key: str, namespace: Optional[List[str]] = None) -> str:
        return os.path.join(self._get_dir(namespace), key)

    def _list(
        self, namespace: Optional[List[str]] = None, strip_prefix: bool = True
    ) -> List[str]:
        prefix = self._get_dir(namespace)
        if not prefix:
            return list(self.data.keys())
        return [
            k[len(prefix) + 1 :] if strip_prefix else k
            for k in self.data
            if k.startswith(prefix)
        ]

    def has(self, key: str, namespace: Optional[List[str]] = None) -> bool:
        return self._get(key, namespace) in self.data

    def list(self, namespace: Optional[List[str]] = None) -> List[str]:
        return self._list(namespace)

    @raise_if_read_only()
    def remove(self, key: Optional[str] = None, namespace: Optional[List[str]] = None):
        if key is not None:
            del self.data[self.get(key, namespace)]
            return
        # Remove all keys in the name space.
        if namespace is not None:
            for k in self._list(namespace, strip_prefix=False):
                del self.data[k]
            return
        # Nuke it all.
        self.data = {}

    def describe(self) -> str:
        return f"{self.__class__.__name__}"

    def _get_dir(self, namespace: Optional[List[str]] = None) -> str:
        namespace = namespace if namespace is not None else []
        if self.base_namespace:
            namespace = self.base_namespace + namespace
        if not namespace:
            return ""
        return os.path.join(*namespace)

    def get_options(self) -> Dict[str, str]:
        return {}


class AzureContainer(BaseModel, FileContainer):
    """
    Azure Data Lake Storage Gen2 based implementation of FileContainer. Data are stored in Azure Blob Storage and
    accessed via the az protocol using the adlfs library.

    https://github.com/dask/adlfs
    https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction
    """

    type: str = Field("AzureDataSource", const=True)

    container_name: Optional[str] = Field(
        default=None, description="If None, will be loaded from settings"
    )
    account_name: Optional[str] = Field(
        default=None, description="If None, will be loaded from settings"
    )
    account_key: Optional[str] = Field(
        default=None, description="If None, will be loaded from settings"
    )
    base_namespace: Optional[List[str]] = None
    overwrite = True
    create_container = True
    read_only: bool = False

    def _get_client(self) -> ContainerClient:
        cc = get_container_client(self.container_name, self.account_key, self.account_name)
        if self.create_container and not cc.exists():
            cc.create_container()
        return cc

    def has(self, key: str, namespace: Optional[List[str]] = None) -> bool:
        cc = self._get_client()
        candidates = list(cc.list_blobs(name_starts_with=self._get_blob_path(key, namespace)))
        matches = list([c for c in candidates if c["name"].split("/")[-1] == key])
        return len(matches) > 0

    def list(self, namespace: Optional[List[str]] = None) -> List[str]:
        blobs = self._get_client().list_blobs(name_starts_with=self._get_dir(namespace))
        prefix = self._get_dir(namespace)
        offset = (len(prefix) + 1) if prefix else 0
        trimmed_blobs = [blob["name"][offset:] for blob in blobs if not blob["size"] == 0]
        return trimmed_blobs

    def _get(self, key: str, namespace: Optional[List[str]] = None) -> str:
        self._get_client()  # ensure container exists
        return f"az://{self.container_name}/{self._get_blob_path(key, namespace)}"

    def read(self, key: str, namespace: Optional[List[str]] = None, mode: str = "rb") -> AnyStr:
        blob_data = self._get_client().download_blob(self._get_blob_path(key, namespace))
        out = blob_data.readall()
        return cast(AnyStr, bytes_to_mode(out, mode))  # Cast required for type compatibility

    @raise_if_read_only()
    def write(
        self,
        key: str,
        value: Union[Iterable[AnyStr], IO[AnyStr]],
        namespace: Optional[List[str]] = None,
    ):
        cc = self._get_client()
        bp = self._get_blob_path(key, namespace)
        cc.upload_blob(bp, value, overwrite=self.overwrite)

    @raise_if_read_only()
    def remove(self, key: Optional[str] = None, namespace: Optional[List[str]] = None):
        # No spec at all, drop the container.
        if (
            key is None
            and namespace is None
            and (self.base_namespace is None or len(self.base_namespace) == 0)
        ):
            return self._get_client().delete_container()
        # No key, delete all files within the name space.
        if key is None:
            logger.info(f"Deleting keys {','.join(self.list(namespace))}")
            for key in self.list(namespace):
                try:
                    self._get_client().delete_blob(self._get_blob_path(key, namespace))
                except HttpResponseError:
                    logger.error(
                        f"Failed to delete {self._get_blob_path(key, namespace)} in {self.container_name}"
                    )
            return
        # Key is specified, just delete that single file.
        self._get_client().delete_blob(self._get_blob_path(key, namespace))

    def describe(self) -> str:
        return f"{self.__class__.__name__}@{self.container_name}"

    def _get_dir(self, namespace: Optional[List[str]] = None) -> str:
        namespace = namespace if namespace is not None else []
        if self.base_namespace:
            namespace = self.base_namespace + namespace
        return "/".join(namespace)

    def _get_blob_path(self, key: str, namespace: Optional[List[str]] = None):
        return os.path.join(self._get_dir(namespace), key)

    def get_options(self) -> Dict[str, str]:
        options = {}
        if self.account_key is not None:
            options["account_key"] = replace_secret_from_key_vault(
                "account_key", self.account_key
            )
        if self.account_name is not None:
            options["account_name"] = self.account_name
        return options


FileContainerTypes = Union[DiskContainer, AzureContainer, DictContainer]
