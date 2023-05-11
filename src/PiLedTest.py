# System imports
import socket
import time
from time import sleep
import RPi.GPIO as GPIO #import RPi.GPIO module
# Local imports

from hal import hal_led as led
from hal import hal_input_switch as switch
from src import PiDemo
import version as ver
def blink_led(delay):
    # Led Blink
    led.init()

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)

def test1(l):
    start = time.time()
    if l:
        while time.time() - start < 5:
            blink_led(0.1)
    else:
        blink_led(0.2)

# 10Hz = blink_led(0.1)
# 5Hz = blink_led(0.2)
def main():
    switch.init()
    switch_status = switch.read_slide_switch()
    test1(switch_status)
if __name__ == "__main__":
    main()