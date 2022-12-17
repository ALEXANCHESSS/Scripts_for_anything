import pyautogui
import time


while True:
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.click()
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)
    print(f'запуск скрипта в {time.asctime()}')
    time.sleep(5*60)