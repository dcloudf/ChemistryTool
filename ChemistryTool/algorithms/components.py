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


__all__ = ['Components']
