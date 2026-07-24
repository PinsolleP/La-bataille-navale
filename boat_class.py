class Boat:
    """Représente un bateau de la flotte."""

    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates
        self.hits = []

    def get_size(self):
        return len(self.coordinates)

    def receive_shot(self, coordinates):
        if coordinates in self.coordinates:
            if coordinates not in self.hits:
                self.hits.append(coordinates)
            return True
        return False

    def is_sunk(self):
        return len(self.hits) == len(self.coordinates)



