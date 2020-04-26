from .abc import ComponentsABC


class Components(ComponentsABC):
    __slots__ = ()

    @property
    def connected_components(self):
        atoms = set(self._atoms)
        bonds = self._bonds

        components = []
        while atoms:
            seen = set()
            queue = [atoms.pop()]
            while queue:
                current = queue.pop(0)
                seen.add(current)
                for n in bonds[current]:
                    if n not in seen:
                        queue.append(n)
            components.append(tuple(seen))
            atoms.difference_update(seen)
        return tuple(components)

    @property
    def connected_components_count(self):
        return len(self.connected_components)

    @property
    def rings_count(self):
        bonds = self._bonds
        return sum(len(x) for x in bonds.values()) // 2 - len(bonds) + self.connected_components_count

    @property
    def get_linked_rings(self):
        while True:
            try:
                loner = (k for k, v in self._bonds.items() if len(v) <= 1)
            except StopIteration:
                break
            del self._atoms[loner]
            for i in self._bonds.pop(loner):
                del self._bonds[i][loner]
        return self._atoms, self._bonds


__all__ = ['Components']
