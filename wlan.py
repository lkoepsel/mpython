# wlan - provides a wireless connection either as main or a function
import time
import network
from machine import Pin, Timer
import secrets
import config
import ubinascii


wireless = Pin("LED", Pin.OUT)
# provide an indication as to why the connection failed
# Connecting to the Internet with Raspberry Pi Pico W
# 3.6.1. Connection status codes
STATUS = ['LINK_BADAUTH',
          'LINK_NONET',
          'LINK_FAIL',
          'LINK_DOWN',
          'LINK_JOIN',
          'LINK_NOIP',
          'LINK_UP']


# simple timer function to blink builtin LED showing wireless status
# slow blink - attempting to connect
# fast blink - connection failed
# off - connection made
def tick(timer):
    global wireless
    wireless.toggle()


# function to call to connect to wireless
def connect():
    global STATUS
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(secrets.ssid, secrets.password)

    # toggle power mode to increase responsiveness
    wlan.config(pm=0xa11140)

    # slow blink to indicate attempting to connect
    blink = Timer()
    blink.init(freq=4, mode=Timer.PERIODIC, callback=tick)

    # attempt 10 times to connect, waiting 1s between attempt
    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        time.sleep(1)

    # Handle connection error by showing fast blink and printing error
    if wlan.status() != 3:
        blink.init(freq=20, mode=Timer.PERIODIC, callback=tick)
        print(f"Connection failed: {STATUS[wlan.status()+3]}")
        return False

    # if connection was successful, provide details as to the wireless signal
    else:
        blink.deinit()
        status = wlan.ifconfig()
        MAC = ubinascii.hexlify(network.WLAN().config('mac'), ':').decode()
        print(f"{wlan.config()}")
        print(f"Name: {config.name}")
        print(f"IP Address: {status[0]}")
        print(f"MAC Address: {MAC}")
        print(f"Channel: {wlan.config('channel')}")
        print(f"SSID: {wlan.config('essid')}")
        print(f"TX Power: {wlan.config('txpower')}")
        return True


if __name__ == '__main__':
    connect()
