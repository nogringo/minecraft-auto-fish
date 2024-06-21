import time
import pyautogui
import keyboard

stop_flag = False
toggle = False

def toggle_script():
    global toggle
    toggle = not toggle
    if toggle:
        pyautogui.mouseDown(button="secondary")
        print("Script activé")
    else:
        pyautogui.mouseUp(button="secondary")
        print("Script désactivé")

def stop_script():
    global stop_flag
    stop_flag = True

# Associer la touche "t" à la fonction toggle_script
keyboard.add_hotkey('t', toggle_script)
keyboard.add_hotkey('y', stop_script)

last_tp_fish_time = time.time()
tp_fish_interval = 1 * 60  # 10 minutes in seconds

while not stop_flag:
    if toggle:
        pyautogui.click()
    time.sleep(0.1)
