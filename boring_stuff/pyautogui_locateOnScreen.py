import pyautogui
from pathlib import Path
import time

print(Path.cwd())
print(Path.cwd() / 'edit2.png')

# b = pyautogui.locateOnScreen(str(Path.cwd() / 'calc7btn.png'), confidence=0.9)
b = pyautogui.locateOnScreen(str(Path.cwd() / 'calc7btn.png'))
print(b)
pyautogui.click(b)
# pyautogui.click(str(Path.cwd() / 'calc7btn.png'))
# time.sleep(0.5)
pyautogui.moveTo(10, 10, duration=0.2)
# pyautogui.click()
# pyautogui.click(str(Path.cwd() / 'calc7btn.png'))
pyautogui.click(b)