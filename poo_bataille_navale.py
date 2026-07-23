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

    def grid_display(grid, columns):
        """
        Affiche la grille de jeu avec numéros de lignes et colonnes.
        - "." : case vide non tirée
        - "O" : tir raté
        - "X" : tir touché
        """
        print("   " + " ".join(columns))

        for line in range(1, 11):
            row_display = []
            for col in columns:
                cell = grid[col][line]
                if cell["touche"]:
                    if cell["boats"]:
                        row_display.append("X")
                    else:
                        row_display.append("O")
                else:
                    row_display.append(".")

            print(f"{line:2} " + " ".join(row_display))


class Game:
    pass
