#! python3
# countdown.py - A simple countdown script

import time, subprocess
timeLeft = 10
while timeLeft > 0:
    print(timeLeft, end=' ')
    time.sleep(1)
    timeLeft -= 1

proc=subprocess.Popen(['start', 'alarm.wav'], shell=True)
# proc.wait()