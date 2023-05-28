# Charge le code nécessaire pour discuter avec le
# contrôleur de jeu
from robots import *

# Ouvre la connexion avec le contrôlleur de robots
with connexion():
    # Sélection du robot que l'on souhaite contrôler 
    utiliser("bleu_1")
    
    print("Envoi du robot dans ses cages")
    definir_couleur("bleu")
    deplacer(-0.8, 0, 0)
    
    print("Replacement de la balle au centre")
    teleporter_balle(0, 0)
    
    print("Envoi du robot au centre")
    definir_couleur("rouge")
    deplacer(-0.05, 0, 0)
    
    print("Tir!")
    tirer()