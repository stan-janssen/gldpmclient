import os

from .storage_provider import MessageDirection, StorageProvider


class FileStorageProvider(StorageProvider):
    def __init__(self, directory: str):
        self.directory = directory
        os.makedirs(self.directory, exist_ok=True)

    def store_xml(self, correlation_id: str, direction: MessageDirection, contents: bytes):
        with open(os.path.join(self.directory, f"{correlation_id}_{direction.value.lower()}.xml"), "wb") as file:
            file.write(contents)
