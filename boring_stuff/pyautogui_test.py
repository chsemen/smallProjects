import pyautogui
wh = pyautogui.size()
print(wh)
print(wh[0])
print(wh.width)

# for i in range(10):
#     pyautogui.moveTo(100, 100, duration=0.25)
#     pyautogui.moveTo(200, 100, duration=0.25)
#     pyautogui.moveTo(200, 200, duration=0.25)
#     pyautogui.moveTo(100, 200, duration=0.25)

# for i in range(10):
#     pyautogui.move(100, 0, duration=0.25)
#     pyautogui.move(0, 100, duration=0.25)
#     pyautogui.move(-100, 0, duration=0.25)
#     pyautogui.move(0, -100, duration=0.25)

print(pyautogui.position())
pyautogui.move(100, 0, duration=0.25)
print(pyautogui.position())
p = pyautogui.position()
print(p[0])
print(p.x)

pyautogui.click(10, 5)