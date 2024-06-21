import time
import pyautogui
import keyboard

def enchant_script():
    old_mouse_pos = pyautogui.position()
    pyautogui.keyDown("shift")
    pyautogui.click()
    pyautogui.click(2060, 760)
    pyautogui.click(1590, 915)
    pyautogui.keyUp("shift")
    pyautogui.moveTo(old_mouse_pos.x + 90, old_mouse_pos.y)

def desenchant_script():
    old_mouse_pos = pyautogui.position()
    pyautogui.keyDown("shift")
    pyautogui.click()
    pyautogui.click(2160, 856)
    pyautogui.keyUp("shift")
    pyautogui.moveTo(old_mouse_pos.x + 90, old_mouse_pos.y)

keyboard.add_hotkey('t', enchant_script)
keyboard.add_hotkey('y', desenchant_script)

keyboard.wait("r")
