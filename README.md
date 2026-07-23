# La-bataille-navale
Programme python POO

# Ce projet est un simulateur du jeu La bataille navale

# Objectifs

Ce projet a été réalisé afin de mettre en pratique les notions suivantes :

-le développement python orienté objet
-l'utilisation de git et de github

# Règlr du jeu :

Réaliser l’exercice « Bataille Navale » effectué lors du module d’algorithmique (cf. 
Pratique_Intro_Algo.pdf > Exercice : Bataille Navale) en utilisant les possibilités de la programmation 
orientée objet. Partir pour cela de l’exercice que vous aviez réalisé lors de ce module, ou de la 
solution qui avait été proposée. 

Grille de départ
La grille de jeu virtuelle est composée de 10 x 10 cases. Une case est identi ée pour le joueur
par une lettre identi ant la colonne (de 'A' à 'J') et un numéro de ligne (ex. : 'B2')
Les navires suivants sont disposés de façon xe dans la grille :
1     
+---+---+---+---+---+---+---+---+---+---+
2     
| A | B | C | D | E | F | G | H | I | J |
3 +----+---+---+---+---+---+---+---+---+---+---+
4|  1 |   |   |   |   |   |   |   |   |   |   |
5 +----+---+---+---+---+---+---+---+---+---+---+
6 |  2 |   | o | o | o | o | o |   |   |   |   |
7 +----+---+---+---+---+---+---+---+---+---+---+
8 |  3 |   |   |   |   |   |   |   |   |   |   |
9 +----+---+---+---+---+---+---+---+---+---+---+
10 |  4 | o |   |   |   |   |   |   |   |   |   |
11 +----+---+---+---+---+---+---+---+---+---+---+
12 |  5 | o |   | o |   |   |   |   | o | o | o |
5
Exercices d'application
13 +----+---+---+---+---+---+---+---+---+---+---+
14 |  6 | o |   | o |   |   |   |   |   |   |   |
15 +----+---+---+---+---+---+---+---+---+---+---+
16 |  7 | o |   | o |   |   |   |   |   |   |   |
17 +----+---+---+---+---+---+---+---+---+---+---+
18 |  8 |   |   |   |   |   |   |   |   |   |   |
19 +----+---+---+---+---+---+---+---+---+---+---+
20 |  9 |   |   |   |   | o | o |   |   |   |   |
21 +----+---+---+---+---+---+---+---+---+---+---+
22 | 10 |   |   |   |   |   |   |   |   |   |   |
23 +----+---+---+---+---+---+---+---+---+---+---+

porte avion (aircraft carrier) en B2 ;
croiseur (cruiser) en A4 ;
contre torpilleur (destroyer) en C5 ;
sous marin (submarine) en H5 ;
torpilleur (torpedo_boat) en E9.

Mécanique de jeu
Le programme af che au départ une grille vide, puis demande à l'inni au joueur les
coordonnées d'un tir, puis indique si ce tir touche un navire (précisant si le navire est coulé à
la suite de plusieurs tirs convergents, et si la partie est nie lorsque le dernier navire est
coulé), puis af che la grille actualisée suite à ce tir, sur laquelle le joueur est en mesure
d'identi er les cases ayant fait l'objet d'un tir raté et celles constituant une partie d'un navire
touché ou coulé (en distinguant les deux cas).

# Fonctionnalités



# Technologies utilisées

- Python 3.14
- Git / GitHub

# Améliorations possibles

