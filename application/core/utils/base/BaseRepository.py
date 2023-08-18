from abc import ABC, abstractmethod


class BaseRepository(ABC):

    @abstractmethod
    def create(self) -> None:
        pass

    @abstractmethod
    def get(self) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def delete(self) -> None:
        pass
