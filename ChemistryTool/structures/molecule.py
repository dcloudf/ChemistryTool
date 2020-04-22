from .abc import MoleculeABC
from ..algorithms import Isomorphism
from ..periodictable.element import Element


class Molecule(Isomorphism, MoleculeABC):
    __slots__ = ('_atoms', '_bonds', '_atoms_backup', '_bonds_backup')

    def get_atom(self, number) -> Element:
        return self._atoms[number]

    def get_bond(self, start_atom, end_atom):
        return self._bonds[start_atom][end_atom]

    def add_atom(self, element, number, charge):
        if not isinstance(number, int):
            raise TypeError('For adding atom should be a integer')
        elif number in self._atoms:
            raise IndexError('This atom has already exist')
        self._atoms[number] = element
        element.attach(self, number)
        self._bonds[number] = {}

    def add_bond(self, start_atom, end_atom, bond_type):
        if start_atom in self._atoms and end_atom in self._atoms:
            if start_atom == end_atom:
                raise ValueError('Atom cannot have a bond with itself')
            elif start_atom in self._bonds[end_atom] or end_atom in self._bonds[start_atom]:
                raise IndexError('Bond has already exist')
            else:
                self._bonds[start_atom][end_atom] = self._bonds[end_atom][start_atom] = bond_type
        else:
            raise KeyError('Before creating a bond you need to create atoms')

    def delete_atom(self, number):
        del self._atoms[number]
        for i in self._bonds.pop(number):
            del self._bonds[i][number]

    def delete_bond(self, start_atom, end_atom):
        del self._bonds[start_atom][end_atom]
        del self._bonds[end_atom][start_atom]

    def update_atom(self, element, number):
        try:
            _ = self._atoms[number]
            self._atoms[number] = element
        except KeyError:
            print('Atom has not exist or have unacceptable index')

    def update_bond(self, start_atom, end_atom, bond_type):
        try:
            if isinstance(bond_type, int):
                raise TypeError('Bond type should be a integer')
            else:
                _ = self._bonds[start_atom][end_atom] = self._bonds[end_atom][start_atom]
                self._bonds[start_atom][end_atom] = self._bonds[end_atom][start_atom] = bond_type
        except KeyError:
            print('Bond has not exist')

    def __enter__(self):
        self._atoms_backup = self._atoms.copy()
        self._bonds_backup = {x: {} for x in self._bonds}
        for number, value in self._bonds.items():
            self._bonds_backup[number] = value.copy()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self._atoms = self._atoms_backup
            self._bonds = {x: {} for x in self._bonds_backup}
            for number, value in self._bonds_backup.items():
                self._bonds[number] = value
            del self._atoms_backup
            del self._bonds_backup
        else:
            del self._atoms_backup
            del self._bonds_backup

    def __str__(self):
        ''.join([f'{x}{[x for x in self._atoms.values()].count(x)}' for x in {x for x in self._atoms.values()}])

    ...


__all__ = ['Molecule']
