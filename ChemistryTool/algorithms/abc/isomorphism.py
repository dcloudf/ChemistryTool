from abc import ABC, abstractmethod
from typing import Dict


class IsomorphismABC(ABC):
    __slots__ = ()

    @abstractmethod
    def get_mapping(self, other) -> Dict[int, int]:
        ...


__all__ = ['IsomorphismABC']
