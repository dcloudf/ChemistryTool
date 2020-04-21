from typing import Dict
from .abc import IsomorphismABC


class Isomorphism(IsomorphismABC):
    __slots__ = ()

    def get_mapping(self, other) -> Dict[int, int]:
        pass


__all__ = ['Isomorphism']
