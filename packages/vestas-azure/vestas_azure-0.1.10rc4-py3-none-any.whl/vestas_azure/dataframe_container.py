import pandas as pd

from typing import List, Optional, Any
from pydantic import BaseModel, Field
from vestas_azure import FileContainerTypes, raise_if_read_only

format_mappings = dict(
    parquet=dict(read=pd.read_parquet, write=pd.DataFrame.to_parquet, extension=".parquet"),
    csv=dict(read=pd.read_csv, write=pd.DataFrame.to_csv, extension=".csv"),
    # add more formats here as needed
)


class DataFrameContainer(BaseModel):
    type: str = Field("DataFrameContainer", const=True)

    file_container: FileContainerTypes
    file_format: str = "parquet"
    read_only: bool = False

    def get(self, key: str, namespace: Optional[List[str]] = None, **kwargs) -> pd.DataFrame:
        return self._format("read")(
            self.file_container.get(self._key(key), namespace),
            storage_options=self.file_container.get_options(),
            **kwargs,
        )

    @raise_if_read_only()
    def set(self, key: str, df: pd.DataFrame, namespace: Optional[List[str]] = None, **kwargs):
        if self.file_container.has(key, namespace):
            self.file_container.remove(key, namespace)
        self._format("write")(
            df,
            self.file_container.get(self._key(key), namespace),
            storage_options=self.file_container.get_options(),
            **kwargs,
        )

    def has(self, key: str, namespace: Optional[List[str]] = None) -> bool:
        return self.file_container.has(self._key(key), namespace)

    def list(self, namespace: Optional[List[str]] = None) -> List[str]:
        ext = self._format("extension")
        matches = [f for f in self.file_container.list(namespace) if f.endswith(ext)]
        return [m[: -len(ext)] for m in matches]

    def _key(self, key) -> str:
        return f"{key}{self._format('extension')}"

    def _format(self, key: str) -> Any:
        try:
            fmt = format_mappings[self.file_format]
        except KeyError:
            raise ValueError(f"Unsupported format: {self.file_format}")
        return fmt[key]
