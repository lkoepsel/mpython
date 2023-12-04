# blink_speeds - demonstrates the different execution speeds of the 3 emitters
# compile with mpy-cross-v6.1 -march=armv6m blink_speeds.py
# @micropython.bytecode - default emitter, uses uP vm to run bytecodes
# @micropython.native - uses the native emitter, which takes each byte code
# and translates it into equivalent ARM-Thumb machine code
# @micropython.viper - emits ARM-Thumb machine code for each byte code,
# and further optimises certain things such as integer arithmetic
# https://www.kickstarter.com/projects/214379695/micro-python-python-for-microcontrollers/posts/664832
from machine import Pin
import time


@micropython.bytecode
def Blink_b():
    led = Pin(2, Pin.OUT)
    for i in range(1000000):
        led.toggle()


@micropython.native
def Blink_n():
    led = Pin(2, Pin.OUT)
    for i in range(1000000):
        led.toggle()


@micropython.viper
def Blink_v():
    led = Pin(2, Pin.OUT)
    for i in range(1000000):
        led.toggle()


def test():
    print(f"\nEmitter speed test")
    print(f"bytecode: ", end='')
    start = time.ticks_us()
    Blink_b()
    end = time.ticks_us()
    print(f"{time.ticks_diff(end, start):,d} us")

    print(f"native: ", end='')
    start = time.ticks_us()
    Blink_n()
    end = time.ticks_us()
    print(f"{time.ticks_diff(end, start):,d} us")

    print(f"viper: ", end='')
    start = time.ticks_us()
    Blink_v()
    end = time.ticks_us()
    print(f"{time.ticks_diff(end, start):,d} us")
