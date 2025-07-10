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
pyautogui.write("previsão do tempo hoje", interval=0.10)
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.screenshot("previsao.png")
pyautogui.alert(text='Previsao gerada na raiz', title='Sucesso!', button='OK')