from abc import ABC, abstractmethod
from enum import StrEnum


class MessageDirection(StrEnum):
    REQUEST = "REQUEST"
    RESPONSE = "RESPONSE"

class StorageProvider(ABC):

    @abstractmethod
    def store_xml(self, correlation_id: str, direction: MessageDirection, contents: bytes):
        raise NotImplementedError()  # pragma: no cover
