from machine import Pin
import time

pin_led = Pin(2, mode=Pin.OUT)

while True:
    pin_led.toggle()
    time.sleep_ms(250)
