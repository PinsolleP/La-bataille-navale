class Boat:
    pass


class Grid:
    def grid_creation(self, columns, lines):
        """
            Crée une grille 10x10 sous forme de dictionnaire.
            Chaque case contient :
              - boats : booléen (True si un bateau est présent)
              - touche : booléen (True si la case a été tirée)
              - boat_id : nom du bateau présent (ou None)
            :return: Dictionnaire représentant la grille.
            """
        grid = {
            col: {line: {"boats": False, "touche": False, "boat_id": None} for line in lines}
            for col in columns}
        return grid


class Game:
    pass
