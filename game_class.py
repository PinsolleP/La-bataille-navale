from grid_class import Grid
from boat_class import Boat


class Game:
    """Gère une partie de bataille navale."""

    def __init__(self, columns, lines):
        self.grid = Grid(columns, lines)
        self.boats = []

    def create_boats(self):

        submarine = Boat("submarine", [("E", 9), ("F", 9)])
        aircraft_carrier = Boat("aircraft carrier", [("A", 4), ("A", 5), ("A", 6), ("A", 7)])
        cruiser = Boat("cruiser", [("B", 2), ("C", 2), ("D", 2), ("E", 2), ("F", 2)])
        destroyer = Boat("destroyer", [("H", 5), ("I", 5), ("J", 5)])
        torpedo_boat = Boat("torpedo_boat", [("C", 5), ("C", 6), ("C", 7)])

        self.boats.extend([submarine, aircraft_carrier, cruiser, destroyer, torpedo_boat])

    






