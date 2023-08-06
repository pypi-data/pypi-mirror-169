import datetime
import glob
import logging
import os
import tempfile
import time
import uuid

from typing import Tuple, Union, Callable, Optional
from adlfs import AzureBlobFile
from azure.storage.blob import (
    BlobServiceClient,
    ContainerClient,
    ContainerSasPermissions,
    generate_container_sas,
)
from vestas_azure.config import settings
from vestas_azure.utils import replace_secret_from_key_vault

logger = logging.getLogger(__name__)


# region Monkey patches


def _in_azure(path: Union[AzureBlobFile, str]) -> bool:
    if isinstance(path, AzureBlobFile):
        return True
    if isinstance(path, str) and path.startswith("az://"):
        return True
    return False


def _parse_az_path(path: str) -> Tuple[str, str]:
    # Unpack path.
    if isinstance(path, AzureBlobFile):
        path = path.path
    # Strip az part if it's there.
    if path.startswith("az://"):
        path = path[5:]
    # Figure out container and blob name.
    elements = path.split("/")
    container, blob_name = elements[0], "/".join(elements[1:])
    return container, blob_name


def _get_tmp_file(blob_name: str) -> str:
    tmp_path = os.path.join(
        tempfile.gettempdir(), str(uuid.uuid4()), blob_name
    )  # TODO: Do we want uuid here?
    tmp_dir = os.path.dirname(tmp_path)
    os.makedirs(tmp_dir, exist_ok=True)
    return tmp_path


def _monkey_patch_read(path: Union[AzureBlobFile, str], original: Callable, *args, **kwargs):
    # Unless the az file system is used, don't change anything.
    if not _in_azure(path):
        return original(path, *args, **kwargs)
    # Setup tmp file.
    container, blob_name = _parse_az_path(path)
    tmp_path = _get_tmp_file(blob_name)
    # Download the file from Azure.
    cc = get_container_client(container_name=container)
    with open(tmp_path, "wb") as download_file:
        download_file.write(cc.download_blob(blob_name).readall())
    # Read it.
    return original(tmp_path, *args, **kwargs)


def _monkey_patch_write(
    self, path: Union[AzureBlobFile, str], original: Callable, *args, **kwargs
):
    if not _in_azure(path):
        return original(self, path, *args, **kwargs)
    # Save to tmp file on disk.
    container, blob_name = _parse_az_path(path)
    tmp_path = _get_tmp_file(blob_name)
    # Upload to Azure.
    original(self, tmp_path, *args, **kwargs)
    with open(tmp_path, "rb") as f:
        # Handle AzureBlobFile object.
        if isinstance(path, AzureBlobFile):
            abf: AzureBlobFile = path
            abf.write(f.read())
            abf.flush(force=True)
        # Handle raw file path.
        else:
            cc = get_container_client(container_name=container)
            cc.upload_blob(name=blob_name, data=f.read())  # type: ignore


def monkey_patch_pd_read_excel():
    """
    This region of code patches the pandas read_excel function to support the az file system.
    """
    import pandas as pd

    original = pd.read_excel

    def monkey_patch(io, **params):
        return _monkey_patch_read(io, original=original, **params)

    pd.read_excel = monkey_patch


def monkey_pd_write_excel():
    """
    This region of code patches the image write function of the pandas excel writer to support the az file system.
    """
    import openpyxl

    original = openpyxl.Workbook.save

    def monkey_save(self, filename):
        return _monkey_patch_write(self, filename, original)

    openpyxl.Workbook.save = monkey_save


def monkey_patch_pil_save():
    """
    This region of code patches the image save function in the PIL library to support the az file system.
    """

    from PIL.Image import Image

    original = Image.save

    def monkey_save(self, fp, *args, format=None, **kwargs):
        return _monkey_patch_write(self, fp, original, *args, format=format, **kwargs)

    Image.save = monkey_save


# Apply monkey patch if PIL is available.
try:
    monkey_patch_pil_save()
    logging.info("Monkey patching PIL to support writing to az file system.")
except ImportError:
    logging.info("PIL not available, unable to monkey patch.")

# Apply monkey patch if openpyxl (and pandas) is available.
try:
    monkey_patch_pd_read_excel()
    monkey_pd_write_excel()
    logging.info("Monkey patching openpyxl to support writing to az file system.")
except ImportError:
    logging.info("Pandas/openpyxl not available, unable to monkey patch.")


# endregion

# region Convenience functions for instantiating Azure related objects and variables


def fallback_to_settings(value: Optional[str], key: str) -> str:
    """If *value* is None, use the value in settings from *key* instead.
    Throws a ValueError if *key* is not in settings.
    """
    if value is not None:
        return value
    fallback = getattr(settings, key)
    if fallback is not None:
        return fallback
    raise ValueError(f"Variable has not been set: {key}")


def get_account_url(account_name: Optional[str] = None) -> str:
    """
    Get account url. If account_name is not provided, it is read from settings.
    """
    return f"https://{get_account_name(account_name)}.blob.core.windows.net/"


def get_container_client(
    container_name: Optional[str] = None,
    credential: Optional[str] = None,
    account_name: Optional[str] = None,
) -> ContainerClient:
    """
    Get container client. If account_name/container_name/account_key is not provided, it is read from settings.
    """
    return ContainerClient(
        account_url=get_account_url(account_name),
        container_name=get_container_name(container_name),
        credential=get_account_key(credential),
    )


def get_blob_service_client(
    account_name: Optional[str] = None, account_key: Optional[str] = None
) -> BlobServiceClient:
    """
    Get blob service client. If account_name/account_key is not provided, it is read from get_settings().
    """
    return BlobServiceClient(
        account_url=get_account_url(account_name),
        credential=get_account_key(account_key),
    )


def get_blob_url(
    blob_name: str,
    container_name: str = None,
    account_name: str = None,
    credential: str = None,
) -> str:
    """
    Get a URL for downloading a particular blob directly from Azure Blob Storage.
    """
    container_name = get_container_name(container_name)
    sas = get_container_sas(container_name, account_name, credential)
    url = get_account_url(account_name=account_name)
    return f"{url}{container_name}/{blob_name}?{sas}"


def get_container_name(container_name: Optional[str] = None) -> str:
    """Get container name. If argument is None, it is read from settings."""
    return fallback_to_settings(container_name, "BLOB_STORAGE_CONTAINER")


def get_account_key(account_key: Optional[str] = None) -> str:
    """Get account key. If argument is None, it is read from settings."""
    return replace_secret_from_key_vault(
        "account_key", fallback_to_settings(account_key, "BLOB_STORAGE_ACCOUNT_KEY")
    )


def get_account_name(account_name: Optional[str] = None) -> str:
    """Get account name. If argument is None, it is read from settings."""
    return fallback_to_settings(account_name, "BLOB_STORAGE_ACCOUNT_NAME")


def get_container_sas(
    container_name: Optional[str] = None,
    account_name: Optional[str] = None,
    account_key: Optional[str] = None,
    expiry_hours: int = 24,
) -> str:
    """
    Get (i.e. generate) a SAS token for a specific container. If account_name/container_name/account_key is not
    provided, it is read from settings. Per default, the token is valid for 24 hours.
    """
    container_sas = generate_container_sas(
        account_name=get_account_name(account_name),
        container_name=get_container_name(container_name),
        account_key=get_account_key(account_key),
        permission=ContainerSasPermissions(read=True, list=True, write=True, delete=True),
        expiry=datetime.datetime.utcnow() + datetime.timedelta(hours=expiry_hours),
    )
    return container_sas


# endregion

# region Extensions of Azure blob storage library (maybe replace by other library at some point)


def upload_dir(
    src_dir: str,
    container_client: Optional[ContainerClient] = None,
    prefix: Optional[str] = None,
    create_container: bool = True,
    overwrite: bool = True,
    **upload_blob_kwargs,
):
    """
    Upload a directory from local disk to Azure blob storage. Optionally, a path prefix inside the blob storage
    container can be provided via the prefix argument.
    """
    container_client = get_container_client() if container_client is None else container_client
    if create_container and not container_client.exists():
        container_client.create_container()
    # deleting "/" to prevent upload_dir from cutting first letter of file's name
    if src_dir[-1] == "/":
        src_dir = src_dir.rstrip(src_dir[-1])
    elements = glob.glob(src_dir + "/**/*", recursive=True)
    for element in elements:
        if os.path.isdir(element):
            continue
        blob = element.replace(src_dir, "")[1:]
        if prefix is not None:
            blob = prefix + blob
        blob_client = container_client.get_blob_client(blob=blob)
        with open(element, "rb") as data:
            logger.debug(f"uploading: {element}")
            blob_client.upload_blob(data, **upload_blob_kwargs, overwrite=overwrite)  # type: ignore


def download_dir(
    dst_dir: str,
    container_client: Optional[ContainerClient] = None,
    fltr: Optional[Callable] = None,
):
    """
    Download a directory form Azure blob storage to local a directory (i.e. on local disk). Optionally, a filtering
    function can be provided via the fltr argument.
    """
    container_client = get_container_client() if container_client is None else container_client
    blob_list = container_client.list_blobs()
    for blob in blob_list:
        if fltr and not fltr(blob):
            continue
        if blob["size"] == 0:
            continue
        blob_client = container_client.get_blob_client(blob=blob)
        download_file_path = os.path.join(dst_dir, blob.name)
        os.makedirs(os.path.dirname(download_file_path), exist_ok=True)
        content = blob_client.download_blob().readall()
        flag = "wb" if isinstance(content, bytes) else "w"
        with open(download_file_path, flag) as download_file:
            download_file.write(blob_client.download_blob().readall())


def duplicate_container(
    cc_src: ContainerClient,
    cc_dest: ContainerClient,
    max_iterations: int = 60,
    skip_if_exists=True,
):
    """
    Performs a copy operation of all files from the source container to the destination container. In case no
    destination container is given a new container will be created. Method will sleep until all files are copied or
    the wait iteration count (default is 60s)  is exceeded. Example of usage,

    from azure.storage.blob import ContainerClient
    from vestas_azure import duplicate_container, configure_logging

    configure_logging(log_level=logging.INFO)
    container_name = "CONTAINER_NAME"
    cc_src = ContainerClient.from_connection_string("SRC_CONNECTION_STRING_WITH_SAS_TOKEN", container_name)
    cc_dst = ContainerClient.from_connection_string("DST_CONNECTION_STRING_WITH_SAS_TOKEN", container_name)
    duplicate_container(cc_src, cc_dst)

    """
    if not cc_dest.exists():
        cc_dest.create_container()
    else:
        logger.warning("Container already exists. Will copy files into given container.")
    blobs = cc_src.list_blobs()
    logger.info(f"Duplicating from {cc_src.container_name} to {cc_dest.container_name}")
    pending_blobs = []
    for blob in blobs:
        if blob.size == 0:
            continue
        bc_src = cc_src.get_blob_client(blob.name)
        bc_dst = cc_dest.get_blob_client(blob.name)
        if skip_if_exists and bc_dst.exists():
            logger.info(f"Skipping {blob.name}")
            continue
        logger.info(f"Copying {blob.name}")
        bc_dst.start_copy_from_url(bc_src.url)
        pending_blobs.append(bc_dst)
    logger.info("All file copy operations have been initiated, awaiting completion.")
    iteration = 0
    while iteration < max_iterations:
        pending_blobs = [
            blob
            for blob in pending_blobs
            if blob.get_blob_properties().copy["status"] != "success"
        ]
        if len(pending_blobs) == 0:
            break
        logger.info(
            f"Not all copies completed (yet), awaiting iteration {iteration} of {max_iterations}."
        )
        time.sleep(1)
        iteration += 1
    logger.info("All file copy operations have completed.")


# endregion
