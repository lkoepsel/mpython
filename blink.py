from machine import Pin
import time
import sys
import uselect


spoll = uselect.poll()
spoll.register(sys.stdin, uselect.POLLIN)


def read1():
    return(sys.stdin.read(1) if spoll.poll(0) else None)


def Blink():
    led = Pin("LED", Pin.OUT)
    key = read1()

    while key is None:
        led.toggle()
        time.sleep_ms(500)
        key = read1()


if __name__ == '__main__':
    Blink()
    sys.exit()
