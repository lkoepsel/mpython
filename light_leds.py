# light_leds - browser-based method of controlling leds
from machine import Pin
from microdot import Microdot, send_file
import sys


yellow = Pin(2, Pin.OUT)
green = Pin(15, Pin.OUT)
white = Pin(16, Pin.OUT)
blue = Pin(22, Pin.OUT)


def set_led(color, level):
    if color == 'WHITE':
        white.value(int(level))
    if color == 'GREEN':
        green.value(int(level))
    if color == 'BLUE':
        blue.value(int(level))
    if color == 'YELLOW':
        yellow.value(int(level))


# Required for WLAN on Pico W, 'machine' indicates Pico-based micropython
# Will not differeniate between Pico and Pico W!
if hasattr(sys.implementation, '_machine'):
    from wlan import connect
    if not (connect()):
        print(f"wireless connection failed")
        sys.exit()


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


@app.route('pico.min.css')
def bulma(request):
    return send_file('./pico.min.css', max_age=31536000)


@app.get('favicon.png')
def favicon(request):
    return send_file('./favicon.png', content_type='image/png')


@app.get('computer.svg')
def computer_svg(request):
    return send_file('./computer.svg',
                     content_type='image/svg+xml', max_age=31536000)


app.run(port=5001, debug=True)
