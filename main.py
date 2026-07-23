#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
jeux de la bataille navale
L'utilisateur tirent sur une grille 10x10 pour tenter de couler tous les bateaux.
"""

from bataille_navale import grid_creation, grid_display

if __name__ == "__main__":
    grid = grid_creation()
    grid_display(grid)
