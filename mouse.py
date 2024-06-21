import pydirectinput
import random
import time

def move_mouse_relative(interval=10):
    while True:
        # Génère des déplacements relatifs aléatoires avec de petites valeurs
        dx = random.randint(-10, 10)
        dy = random.randint(-10, 10)
        pydirectinput.moveRel(dx, dy, duration=0.1)  # Déplace la souris de manière relative
        time.sleep(interval)

if __name__ == "__main__":
    print("Déplacement de la souris toutes les 10 secondes. Appuyez sur Ctrl+C pour arrêter.")
    move_mouse_relative(10)  # Déplace la souris toutes les 10 secondes
