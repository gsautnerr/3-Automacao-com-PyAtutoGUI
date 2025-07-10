import pyautogui
import time

# pyautogui.moveTo(1780, 16, duration=0.7)
# time.sleep(1)
# pyautogui.click()
# time.sleep(1)
# pyautogui.screenshot("testescreen.png")
# pyautogui.alert(text='Screenshot registrado com êxito', title='Sucesso!', button='OK')

while True:
    pyautogui.screenshot(f"image_{time.time()}.png")
    time.sleep(3)