import pyautogui
import time

# 240,80

pyautogui.press("winleft")
time.sleep(1)
pyautogui.write("chrome")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.moveTo(900, 602, duration=0.7)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(240, 80, duration=0.7)
pyautogui.click()
pyautogui.write("ibovespa hoje", interval=0.10)
time.sleep(1)

pyautogui.press("enter")
time.sleep(1)
pyautogui.screenshot("ibovespa.png")
pyautogui.alert(text='Gerada a imagem na raiz', title='Sucesso!', button='OK')