# blink_key - a blocking blink for built-in led and will stop on any key press
from machine import Pin, Timer
import time
import sys
import uselect


spoll = uselect.poll()
spoll.register(sys.stdin, uselect.POLLIN)

led = Pin("LED", Pin.OUT)
tim = Timer()


def tick(timer):
    global led
    led.toggle()


def read1():
    return sys.stdin.read(1) if spoll.poll(0) else None


if __name__ == "__main__":
    tim.init(freq=1.5, mode=Timer.PERIODIC, callback=tick)
    key = read1()
    if key is not None:
        tim.deinit()
        led.value(0)
        print("Key pressed, exiting...")
        sys.exit()
