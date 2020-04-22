from abc import ABC, abstractmethod
from typing import Tuple


class ComponentsABC(ABC):
    __slots__ = ()

    @property
    @abstractmethod
    def connected_components(self) -> Tuple[Tuple[int, ...], ...]:
        ...

    @property
    @abstractmethod
    def connected_components_count(self) -> int:
        ...

    @property
    @abstractmethod
    def rings_count(self) -> int:
        ...


__all__ = ['ComponentsABC']
