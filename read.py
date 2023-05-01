import time


time.sleep(2)
f = open('delay.txt', 'r')
delay = int(f.read())
print(delay, delay / 2)
