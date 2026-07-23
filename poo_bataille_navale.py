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

    def grid_display(self, columns):
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
                cell = self[col][line]
                if cell["touche"]:
                    if cell["boats"]:
                        row_display.append("X")
                    else:
                        row_display.append("O")
                else:
                    row_display.append(".")

            print(f"{line:2} " + " ".join(row_display))

    def place_boat(self, start, end, boat_name, columns):
        """
        Place un bateau sur la grille entre deux coordonnées.
        :param self: Grille de jeu.
        :param start: Coordonnée de départ (ex : 'A4').
        :param end: Coordonnée de fin (ex : 'A7').
        :param boat_name: Nom du bateau.
        :return: Liste des coordonnées occupées par le bateau.
        """
        start_col, start_line = start[0], int(start[1:])
        end_col, end_line = end[0], int(end[1:])
        coords = []

        # Placement horizontal
        if start_line == end_line:
            for col in columns[columns.index(start_col):columns.index(end_col) + 1]:
                self[col][start_line]["boats"] = True
                self[col][start_line]["boat_id"] = boat_name
                coords.append((col, start_line))

        # Placement vertical
        elif start_col == end_col:
            for line in range(start_line, end_line + 1):
                self[start_col][line]["boats"] = True
                self[start_col][line]["boat_id"] = boat_name
                coords.append((start_col, line))

        return coords


class Game:
    pass
