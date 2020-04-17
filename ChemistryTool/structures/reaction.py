from .abc import ReactionABC, MoleculeListABC
from .molecule import Molecule
from collections import Iterable


class MoleculeList(MoleculeListABC):
    def insert(self, i, molecule):
        if isinstance(molecule, Molecule):
            self._data.insert(i, molecule)
        else:
            raise TypeError('Only Molecule acceptable')

    def __getitem__(self, i):
        if isinstance(i, slice):
            ml = object.__new__(MoleculeList)
            ml._data = self._data[i]
            return ml
        return self._data[i]

    def __setitem__(self, i, molecule):
        if isinstance(i, slice):
            if issubclass(molecule, Iterable):
                self._data[i] = molecule
            else:
                raise TypeError('Can set only for iterable data')
        elif isinstance(i, int) and isinstance(molecule, Molecule):
            self._data[i] = molecule
        else:
            return TypeError

    def __repr__(self):
        return self._data


class Reaction(ReactionABC):
    def __init__(self):
        super().__init__()
        self._reactants = MoleculeList()
        self._products = MoleculeList()

    @property
    def reactants(self):
        return self._reactants

    @property
    def products(self):
        return self._products


__all__ = ['Reaction']
