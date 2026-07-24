class Grid:
    def __init__(self, columns, lines):
        """
                    Crée une grille 10x10 sous forme de dictionnaire.
                    Chaque case contient :
                      - boats : booléen (True si un bateau est présent)
                      - touche : booléen (True si la case a été tirée)
                      - boat_id : nom du bateau présent (ou None)
                    """
        self.columns = columns
        self.lines = lines

        grid = {
            col: {line: {"boats": False, "touche": False, "boat_id": None} for line in self.lines}
            for col in self.columns}
        self.grid = grid

    def grid_display(self):
        """
        Affiche la grille de jeu avec numéros de lignes et colonnes.
        - "." : case vide non tirée
        - "O" : tir raté
        - "X" : tir touché
        """
        print("   " + " ".join(self.columns))

        for line in range(1, 11):
            row_display = []
            for col in self.columns:
                cell = self.grid[col][line]
                if cell["touche"]:
                    if cell["boats"]:
                        row_display.append("X")
                    else:
                        row_display.append("O")
                else:
                    row_display.append(".")

            print(f"{line:2} " + " ".join(row_display))

    def place_boat(self, boat):

        for col, line in boat.coordinates:
            self.grid[col][line]["boats"] = True
            self.grid[col][line]["boat_id"] = boat.name




