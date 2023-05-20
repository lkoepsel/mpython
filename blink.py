from machine import Pin
import time


def Blink():
    led = Pin("LED", Pin.OUT)

    while True:
        led.toggle()
        time.sleep_ms(250)


if __name__ == '__main__':
    Blink()
