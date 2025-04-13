import pyautogui

pyautogui.sleep(2)
print('Starting in ', end=''); pyautogui.countdown(3)
pyautogui.click()
pyautogui.write(['a', 'b', 'left', 'left', 'X', 'Y'], interval=0.2)
pyautogui.press(['home'], interval=0.2)
pyautogui.keyDown('shiftleft'); pyautogui.press(['end']); pyautogui.keyUp('shiftleft')
# pyautogui.sleep(1)
# pyautogui.hotkey('ctrl', 'c')
# pyautogui.sleep(1)
# pyautogui.write(['enter'], interval=0.2)
# pyautogui.sleep(1)
# pyautogui.hotkey('ctrl', 'v')
# pyautogui.sleep(2)
# pyautogui.hotkey('ctrl', 'v')

