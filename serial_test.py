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
# Thonny was required to regain control of board

import time
import machine


f = open('delay.txt', 'r')
delay = int(f.read())
time.sleep_ms(delay)
print("Hello World!", delay)
f.close()

f = open('delay.txt', 'w')
delay += 10
f.write(str(delay))
f.close()
machine.reset()
