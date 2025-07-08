import pyautogui
import time

#1- Pegar o tamanho da tela
print(pyautogui.size())

#2- Pega a posição atual do cursor
print(pyautogui.position())

#3- Aplicação para ver a posição do mouse em tempo real
"""
Digite o comando python no terminal
from pyautogui import mouseInfo
mouseInfo()
"""

#4- Mover o cursor do mouse

pyautogui.moveTo(1777, 20, duration=0.7)
time.sleep(1)
pyautogui.click()

#5- Realizando o Scroll

pyautogui.moveTo(1060, 461)
pyautogui.click()
time.sleep(1)
pyautogui.scroll(6000)


