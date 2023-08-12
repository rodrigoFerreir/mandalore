from abc import ABC, abstractmethod


class BaseService(ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def create() -> None:
        pass

    @abstractmethod
    def get() -> None:
        pass

    @abstractmethod
    def update() -> None:
        pass

    @abstractmethod
    def delete() -> None:
        pass
