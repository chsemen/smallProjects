import pyautogui
import time

fw = pyautogui.getActiveWindow()
print(fw.width)
print(fw.topleft)
fw.width = 1000
time.sleep(2)
fw.topleft = (800,400)
print(fw.isMaximized)
print(fw.isActive)

time.sleep(2)
fw.maximize()
print(fw.isMaximized)
time.sleep(2)
fw.restore()
time.sleep(2)
fw.minimize()
time.sleep(2)
fw.restore()
fw.activate()
# fw.close()