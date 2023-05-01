# pin_test.py - interactive app to test pins on a board
# uses pin number (1-40) as the reference number
import machine
import time

PicoW_pins = [[0, 'UART0 TX'],      # Pin 1
              [0, 'UART0 RX'],
              [0, 'GND'],
              [1, 'GP2'],
              [1, 'GP3'],
              [1, 'GP4'],
              [1, 'GP5'],
              [0, 'GND'],
              [1, 'GP6'],
              [1, 'GP7'],         # Pin 10
              [1, 'GP8'],
              [1, 'GP9'],
              [0, 'GND'],
              [1, 'GP10'],
              [1, 'GP11'],
              [1, 'GP12'],
              [1, 'GP13'],
              [0, 'GND'],
              [1, 'GP14'],
              [1, 'GP15'],         # Pin 20
              [1, 'GP16'],
              [1, 'GP17'],
              [0, 'GND'],
              [1, 'GP18'],
              [1, 'GP19'],
              [1, 'GP20'],
              [1, 'GP21'],
              [0, 'GND'],
              [1, 'GP22'],
              [0, 'RUN'],         # Pin 30
              [0, 'ADC0'],
              [0, 'ADC1'],
              [0, 'AGND'],
              [0, 'ADC2'],
              [0, 'ADC_REF'],
              [0, '3V3(OUT)'],
              [0, '3V3_EN'],
              [0, 'GND'],
              [0, 'VSYS'],
              [0, 'VBUS']         # Pin 40
              ]

minTest = 1
maxTest = 3

maxPins = 40


def print_header():
    print("Running Pin Test:")
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
    pin = int(input("Enter pin number (1-40) to test: "))
    if (pin > maxPins):
        print("Error, pin requested", pin,
              " > number of board pins:", maxPins)
        pin = -1
    elif (pin < 0):
        print("Error, pin requested", pin, " < 0:")
        pin = -1
    else:
        if PicoW_pins[pin][0]:
            print(pin, PicoW_pins[pin][1], " enabled as Output")
        else:
            print(pin, PicoW_pins[pin][1], "is not a GPIO pin")
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
