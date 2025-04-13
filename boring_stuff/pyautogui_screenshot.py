import pyautogui
im  = pyautogui.screenshot()

print(pyautogui.pixel(0, 0))
print(pyautogui.pixel(50, 200))

print(pyautogui.pixelMatchesColor(50, 200, (117, 117, 117)))
print(pyautogui.pixelMatchesColor(50, 200, (24, 24, 24)))
