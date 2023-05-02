# wlan_v2 - wireless lan connection, use LEDs for status
import time
import network
import machine
import secrets
from microdot import Microdot


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.ssid, secrets.password)

wait = machine.Pin(2, machine.Pin.OUT)
connected = machine.Pin(15, machine.Pin.OUT)
server = machine.Pin(16, machine.Pin.OUT)
# Indicate waiting to connect
wait.value(1)

max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    time.sleep_ms(500)
    wait.toggle()
    time.sleep_ms(500)
    wait.toggle()


# Handle connection error
if wlan.status() != 3:
    while True:
        wait.toggle()
        time.sleep_ms(50)
        wait.toggle()
        time.sleep_ms(50)

else:
    wait.value(0)
    connected.value(1)
    status = wlan.ifconfig()


app = Microdot()


@app.route('/')
def index(request):
    server.value(1)
    return 'Hello, world!'


app.run()
