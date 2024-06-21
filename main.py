import time
import pyautogui
import keyboard
import pydirectinput
import random

stop_flag = False
toggle = False
road_durability = None
mouse_rel_x = 0

with open('road_durability.txt', 'r', encoding='utf-8') as fichier:
    road_durability = int(fichier.read())

def toggle_script():
    global toggle
    toggle = not toggle
    if toggle:
        print("Script activé")
    else:
        print("Script désactivé")

def stop_script():
    global stop_flag
    stop_flag = True

# Associer la touche "t" à la fonction toggle_script
keyboard.add_hotkey('t', toggle_script)
keyboard.add_hotkey('y', stop_script)

def repair_road():
    global road_durability

    # open chat
    pyautogui.keyDown("ENTER")
    pyautogui.keyUp("ENTER")

    # type /forgeron
    pyautogui.typewrite("/forgeron")

    # send command
    pyautogui.keyDown("ENTER")
    pyautogui.keyUp("ENTER")

    # click anvil 1920, 860
    pyautogui.click(1920, 860)

    # click anvil 1920, 680
    pyautogui.click(1920, 680)

    road_durability = 1250

def tp_fish():
    # open chat
    pyautogui.keyDown("ENTER")
    pyautogui.keyUp("ENTER")

    # type /forgeron
    pyautogui.typewrite("/v home")

    # send command
    pyautogui.keyDown("ENTER")
    pyautogui.keyUp("ENTER")

    time.sleep(5)

last_tp_fish_time = time.time()
tp_fish_interval = 1 * 60  # 10 minutes in seconds

while not stop_flag:
    if toggle:
        quitter_btn_location = pyautogui.locateOnScreen(image="quitter_btn.png", confidence=0.9, region=(2087, 981, 207, 35))
        if quitter_btn_location is not None:
            pyautogui.moveTo(pyautogui.center(quitter_btn_location), duration=1)
            time.sleep(1)
            pyautogui.click(duration=1)
            time.sleep(1)
            tp_fish()
            time.sleep(5)
            pyautogui.rightClick()


        indicator_location = pyautogui.locateOnScreen(image="indicator.png", confidence=0.8, region=(3176, 1000, 613, 1160))
        if indicator_location is not None:
            pyautogui.rightClick()
            time.sleep(0.5)

            # road_durability = road_durability - 1
            # if road_durability < 10:
            #     repair_road()

            time.sleep(0.5)
            pyautogui.rightClick()
            time.sleep(1)
            time.sleep(1)
    time.sleep(0.1)
