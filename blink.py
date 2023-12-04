# blink - the classic, can be used as a program or as a function
from machine import Pin
import time


def Blink():
    led = Pin("LED", Pin.OUT)

    while True:
        led.toggle()
        time.sleep_ms(250)


if __name__ == '__main__':
    Blink()
