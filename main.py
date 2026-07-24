#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
jeux de la bataille navale
L'utilisateur tirent sur une grille 10x10 pour tenter de couler tous les bateaux.
"""
from grid_class import Grid
from boat_class import Boat

columns = [chr(c) for c in range(ord('A'), ord('J') + 1)]
lines = range(1, 11)

if __name__ == "__main__":
    grid = Grid(columns, lines)
    grid.grid_display()

    submarine = Boat(
        "submarine",
        [
            ("E", 9),
            ("F", 9)
        ]
    )

    print(submarine.name)
    print(submarine.get_size())

    print(submarine.is_sunk())

    submarine.receive_shot(("E", 9))
    print(submarine.is_sunk())

    submarine.receive_shot(("F", 9))
    print(submarine.is_sunk())

