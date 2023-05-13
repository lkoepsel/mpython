# determines delay required for serial connection
# uses file delay.txt to contain a integer delay i.e; 1000
# program will:
#   read delay from delay.txt
#   pause delay ms
#   print 'hello world' and delay value
#   incr delay
#   hard reset to repeat
# this will continue until 'Hello World' and delay are seen
# the delay shown is the ms required to sleep prior to using serial
# in testing 1390 was the delay shown
# Added max test to ensure test completes, otherwise
# Thonny required to stop the microcontroller

import time
import machine
import sys


f = open('delay.txt', 'r')
delay = int(f.readline())
delta = 10
time.sleep_ms(delay)
print("Hello World!", delay)
f.close()

f = open('delay.txt', 'w')
delay += delta
f.write(str(delay))
f.close()

if delay <= 1700:
    machine.reset()
else:
    sys.exit()
