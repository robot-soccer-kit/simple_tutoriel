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
        deplacer(balle_x, 0, 0, attendre=False)
        
        # Si la balle est à gauche, le robot sera
        # vert. Sinon il sera bleu
        if balle_x < 0:
            definir_couleur("vert")
        else:
            definir_couleur("bleu")
        
        # Attendre un peu
        attendre()
        