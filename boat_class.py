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






    #def check_sink(self, boat_name, grid):
        """
        Vérifie si toutes les cases d'un bateau sont touchées.
        :param grid: Grille de jeu.
        :param boat_name: Nom du bateau.
        :return: True si le bateau est coulé, False sinon.
        """
        for col in self.coordinates:
            for line in self.coordinates:
                cell = self.coordinates[col][line]
                if cell["boats"] and cell["boat_id"] == boat_name and not cell["touche"]:
                    return False
        return True


