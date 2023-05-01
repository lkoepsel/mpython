# PinTest.py - interactive app to test pins on a board
import machine
import time


minTest = 1
maxTest = 3

maxPins = 29


def print_header():
    print("Running Pin Test")
    print("""Tests: 0=> new pin 1=> High 2=> Low  3=> Blink once""")


def PinTest():
    startState = True
    testState = True
    print_header()

    while startState:
        pin = getPin()
        if pin >= 0:
            startState = False
            pinT = machine.Pin(pin, machine.Pin.OUT)

    while testState:
        test = getTest()
        if test >= 0:
            if test == 0:
                startState = True
                testState = False

            elif test == 1:  # 1 - set pin HIGH
                runTest_1(pinT)
                testState = True

            elif test == 2:  # 1 - set pin LOW
                runTest_2(pinT)
                testState = True

            elif test == 3:  # 1 - set pin to BLINK
                runTest_3(pinT)
                testState = True

            else:  # print error, not a valid test number
                print(test, "entered. Must be 0, 1, 2, or 3")
                testState = True


def getPin():
    pin = int(input("Enter pin to test: "))
    if (pin > maxPins):
        print("Error, pin requested", pin,
              " > number of output pins:", maxPins)
        pin = -1
    elif (pin < 0):
        print("Error, pin requested", pin, " < 0:")
        pin = -1
    else:
        print(pin, " enabled as Output")
    return(pin)


def getTest():
    test = int(input("Enter test to run: "))
    if test > maxTest:
        print("Error, test requested", test, "> tests allowed ")
        test = -1
    elif (test == 0):
        print("Restarting")
    elif test < minTest:
        print("Error, test requested", test, "< 0")
        test = -1
    return(test)


def blink(pin):
    pin.value(1)  # sets the digital pinN on
    time.sleep_ms(50)            # waits for a second
    pin.value(0)  # sets the digital pinN on
    time.sleep_ms(50)            # waits for a second


def runTest_1(pin):
    pin.value(1)
    print(pin, " is High")


def runTest_2(pin):
    pin.value(0)
    print(pin, " is LOW")


def runTest_3(pin):
    print(pin, " will blink once")
    blink(pin)


# delay required for serial connection to start
time.sleep_ms(1400)
while True:
    PinTest()
