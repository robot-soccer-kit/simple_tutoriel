import math
import time
import rsk

client: rsk.Client = None
robot: rsk.client.ClientRobot = None

class connexion:
    def __init__(self, hote:str = "127.0.0.1"):
        global client
        client = rsk.Client(host=hote)
        
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, tb):
        client.stop()

    
def utiliser(nom: str):
    global robot
    
    robots = {
        "bleu_1": client.blue1,
        "bleu_2": client.blue2,
        "vert_1": client.green1,
        "vert_2": client.green2,
    }
    
    if nom in robots:
        robot = robots[nom]
    else:
        print(f"Robot inconnu: {nom}, robots disponibles: {', '.join(robots.keys())}")
        exit()
        
def deplacer(x: float, y:float, alpha: float, attendre_arrivee: bool = True):
    robot.goto((x, y, math.radians(alpha)), wait=attendre_arrivee)

def teleporter_balle(x: float, y: float):
    client.teleport_ball(x, y)

def definir_couleur(couleur: str):
    colors = {
        "rouge": (255, 0, 0),
        "vert": (0, 255, 0),
        "bleu": (0, 0, 255),
        "jaune": (255, 255, 0),
        "rose": (255, 0, 255),
        "cyan": (0, 255, 255),
        "off": (0, 0, 0),
        "blanc": (255, 255, 255),
        "orange": (255, 64, 0)
    }
    
    if couleur in colors:
        robot.leds(*colors[couleur])
    else:
        print(f"Couleur inconnu: {couleur}, couleurs disponibles: {', '.join(colors.keys())}")
        exit()
        
def tirer():
    global robot
    
    robot.kick()
    
def position_balle():
    return client.ball

def position_robot():
    return robot.position

def attendre(temps: float = (1/30.)):
    time.sleep(temps)