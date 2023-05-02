# wlan_v2 - wireless lan connection, use LEDs for status
import time
import network
from machine import Pin, Timer
import secrets
from microdot import Microdot


wireless = Pin("LED", Pin.OUT)
yellow = Pin(2, Pin.OUT)
green = Pin(15, Pin.OUT)
white = Pin(16, Pin.OUT)
blue = Pin(22, Pin.OUT)


def tick(timer):
    global wireless
    wireless.toggle()


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.ssid, secrets.password)

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

else:
    blink.deinit()


app = Microdot()


@app.route('/')
def index(request):
    return 'Hello from Pico W'


@app.route('/white')
def white_led(request):
    global white
    white.toggle()
    return 'white LED will toggle'


@app.route('/green')
def green_led(request):
    global green
    green.toggle()
    return 'green LED will toggle'


@app.route('/yellow')
def yellow_led(request):
    global yellow
    yellow.toggle()
    return 'yellow LED will toggle'


@app.route('/blue')
def blue_led(request):
    global blue
    blue.toggle()
    return 'blue LED will toggle'


app.run()
