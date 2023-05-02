# wlan_v3 - wireless lan connection, use built-in LED for status
import time
import network
from machine import Pin, Timer
import secrets
import sys


def tick(timer):
    global wireless
    wireless.toggle()


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.ssid, secrets.password)

wireless = Pin("LED", Pin.OUT)
blink = Timer()

max_wait = 10
blink.init(freq=4, mode=Timer.PERIODIC, callback=tick)
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    time.sleep(1)


# Handle connection error
if wlan.status() != 3:
    blink.init(freq=20, mode=Timer.PERIODIC, callback=tick)
    print('Unable to connect')

else:
    blink.deinit()
    status = wlan.ifconfig()
    print('ip = ' + status[0])
    status = wlan.ifconfig()
    sys.exit()
