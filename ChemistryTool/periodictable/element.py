from typing import Optional, TYPE_CHECKING
from weakref import ref

if TYPE_CHECKING:
    from ChemistryTool.structures import Molecule


class Element:
    __slots__ = ('isotope', '_mol', '_num')

    def __init__(self, isotope: Optional[int] = None):
        self.isotope = isotope

    def attach(self, mol: 'Molecule', number: int):
        if hasattr(self, '_mol'):
            raise Exception('atom already attached')
        self._mol = ref(mol)
        self._num = number

    @property
    def charge(self):
        return self._mol()._charges[self._num]


__all__ = ['Element']
