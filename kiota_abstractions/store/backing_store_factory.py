from abc import ABC, abstractmethod

from .backing_store import BackingStore


class BackingStoreFactory(ABC):
    """Defines the contract for a factory that creates backing stores.
    """

    @abstractmethod
    def create_backing_store(self) -> BackingStore:
        """Creates a new instance of the backing store.

        Returns:
            BackingStore:a new instance of the backing store.
        """
        pass
