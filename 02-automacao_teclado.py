import pyautogui
import time

# pyautogui.write("Ola mundo!")

# Código para abrir calculadora

pyautogui.press("winleft")
time.sleep(1)
pyautogui.write("calculadora")
pyautogui.press("enter")

# pyautogui.keyDown('alt')
# pyautogui.press('f4')

# tecla de atalho
# pyautogui.hotkey("ctrl", "shift", "esc")

pyautogui.keyDown("winleft")
pyautogui.press(["left"])
time.sleep(2)
pyautogui.keyDown("winleft")
pyautogui.press(["right"])

