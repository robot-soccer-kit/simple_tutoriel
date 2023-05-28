# Charge le code nécessaire pour discuter avec le
# contrôleur de jeu
from robots import *

# Ouvre la connexion avec le contrôlleur de robots
with connexion():
    # Sélection du robot que l'on souhaite contrôler 
    utiliser("bleu_1")
    # Amène le robot dans ses cages
    deplacer(-0.8, 0, 0)
    
    while True:
        # Obtient la position de la balle
        balle_x, balle_y = position_balle()

        # Se déplace vers la balle
        deplacer(balle_x - 0.2, balle_y, 0)
