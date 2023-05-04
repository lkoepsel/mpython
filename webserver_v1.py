# wlan_v2 - wireless lan connection, use LEDs for status
import time
import network
from machine import Pin, Timer
import secrets
from microdot import Microdot, send_file


wireless = Pin("LED", Pin.OUT)
yellow = Pin(2, Pin.OUT)
green = Pin(15, Pin.OUT)
white = Pin(16, Pin.OUT)
blue = Pin(22, Pin.OUT)


def tick(timer):
    global wireless
    wireless.toggle()


def set_led(color, level):
    if color == 'WHITE':
        white.value(int(level))
    if color == 'GREEN':
        green.value(int(level))
    if color == 'BLUE':
        blue.value(int(level))
    if color == 'YELLOW':
        yellow.value(int(level))


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
    status = wlan.ifconfig()
    print('ip = ' + status[0])


app = Microdot()


@app.route('/')
def index(request):
    return send_file('./index.html')


@app.post('/')
def index_post(request):
    level = request.form['level']
    led = request.form['led']
    print("Set", led, "led", level)
    set_led(led, level)
    return send_file('./index.html')


@app.route('bulma.min.css')
def bulma(request):
    return send_file('./bulma.min.css')


@app.get('favicon.png')
def favicon(request):
    return send_file('./favicon.png', content_type='image/png')


@app.get('computer.svg')
def computer_svg(request):
    return send_file('./computer.svg', content_type='image/svg+xml')


@app.get('blue.svg')
def blue_svg(request):
    return send_file('./blue.svg', content_type='image/svg+xml')


@app.get('white.svg')
def white_svg(request):
    return send_file('./white.svg', content_type='image/svg+xml')


@app.get('green.svg')
def green_svg(request):
    return send_file('./green.svg', content_type='image/svg+xml')


@app.get('yellow.svg')
def yellow_svg(request):
    return send_file('./yellow.svg', content_type='image/svg+xml')


@app.route('/blue')
def blue_led(request):
    global blue
    blue.toggle()
    return send_file('./index.html')


@app.route('/white')
def white_led(request):
    global white
    white.toggle()
    return send_file('./index.html')


@app.route('/green')
def green_led(request):
    global green
    green.toggle()
    return send_file('./index.html')


@app.route('/yellow')
def yellow_led(request):
    global yellow
    yellow.toggle()
    return send_file('./index.html')


app.run(debug=True)
