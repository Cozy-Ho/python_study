import pyautogui as m
import time
import random

count = 0
while True:
    set = random.randint(5, 9)
    time.sleep(set*60)
    x, y = m.position()
    if set % 2 == 0:
        m.moveTo(x+5, y+5)
    else:
        m.moveTo(x-5, y-5)
    count += 1
    print('x : {}, y: {}, count:{}'.format(x, y, count))
