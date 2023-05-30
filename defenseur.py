# Charge le code nécessaire pour discuter avec le
# contrôleur de jeu
from robots import *

# Ouvre la connexion avec le contrôlleur de robots
with connexion():
    # Sélection du robot que l'on souhaite contrôler 
    utiliser("bleu_1")
    
    # Ceci est une boucle qui se répètera à l'infini!
    while True:
        balle_x, balle_y = position_balle()
        print(f"Position de la balle {balle_x}, {balle_y}")
        
        # Le robot se déplace au même x que la balle
        deplacer(balle_x, 0, 0, attendre_arrivee=False)
        
        # Si la balle est à gauche, le robot sera vert
        # si elle est au centre, il sera jaune,
        # si elle est à droite, il sera rouge
        if balle_x < -0.3:
            definir_couleur("vert")
        elif balle_x < 0.3:
            definir_couleur("jaune")
        else:
            definir_couleur("rouge")
        
        # Attendre un peu
        attendre()
        