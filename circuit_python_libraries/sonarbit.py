# Write your code here :-)

""" Sonarbit Distance Program.
This program is accurate >5cm < 110cm (unless the object is very large),
It will crash if an object is touching the reading.
Some sort of 'try' needs to be implemented"""

import time
import board
import digitalio
from math import floor

def sonar(pin):
    usleep = lambda x: x/1000000

    pin.direction = digitalio.Direction.OUTPUT

    #send trigger signal
    pin.value = 0
    usleep(2)
    pin.value = 1
    usleep(10)
    pin.value = 0

    pin.direction = digitalio.Direction.INPUT
    while pin.value == 0:
        start_time = time.monotonic_ns()

    while pin.value == 1:
        end_time = time.monotonic_ns()

    # Distance is defined as time/2 (there and back) * speed of sound 34000 cm/s
    distance = floor((end_time - start_time) * 34000/2/1000000000)
    return distance


pin = digitalio.DigitalInOut(board.D7)
while True:
    print("the object is " + str(sonar(pin)) + " cm away")
    time.sleep(0.5)

