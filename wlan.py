import time
import network
import machine
import secrets


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

pinW = machine.Pin(2, machine.Pin.OUT)
pinC = machine.Pin(15, machine.Pin.OUT)
# Wait for connect or fail
pinW.value(1)

max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    pinW.value(0)
    pinC.value(1)
    print('connected')
    status = wlan.ifconfig()
    print('ip = ' + status[0])
