'''Mobile Robot Test
Initial test for a mobile robot using the RoboClaw 2x7A motor controller

Pin Diagram: 
D0 > S1/M1 on Roboclaw
D1 > S2/M2 on Roboclaw
D2 > Ping Sensor
D3 > Debug x16 Neopixel Ring

Roboclaw:
Running Mode 1, Opt 4 for tank style driving (non-differential)
S1 = M1 direction/speed
S2 = M2 direction/speed

MCU mode is enabled, so the RC will not auto-calibrate itself to a centre point on an RC controller initially, instead, it uses to following servo pulses:
Min: 1120us
Stop: 1520us
Max: 1920us


'''

import time
import board
import digitalio
import pwmio
import neopixel
from math import floor

rc_m1 = pwmio.PWMOut(board.D0, frequency=50)
rc_m2 = pwmio.PWMOut(board.D1, frequency=50)
sonarbit = digitalio.DigitalInOut(board.D2)
pixel_ring = neopixel.NeoPixel(board.D3, 16, brightness=0.1)



#Colours for neopixel
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
OFF = (0,0,0)

def neopixel_ring_debug(COLOUR):
    ''' Displays a x16 solid colour on the neopixel ring
    COLOUR = (0,0,0) list for Red, Gree, Blue values respectively
    '''
    pixel_ring.fill(COLOUR)
    pixel_ring.show

def ms_duty_cycle_convert(pulse_ms, frequency=50):
    '''converts a millisecond pulse command into a duty cycle value (0>65535) that circuitpython understands
    pulse_ms = a value in ms. In this case, us are desired, so 1520us = 1.520ms
    frequency = 50, the default argument we want to send servo pulses in. In the roboclaw and standard servo case, this is 50Hz. 

    returns converted ms > duty_cycle value between 0>65535 that circuitpy understands, and outputs as a PWM 
    '''

    period_ms = 1.0 / frequency * 1000.0
    duty_cycle = int(pulse_ms / (period_ms / 65535.0))
    return duty_cycle

def sonar_bit(pin):
    ''' Sonarbit Distance Program.
    This program is accurate >5cm < 110cm (unless the object is very large),
    It will crash if an object is touching the reading.
    Some sort of 'try' needs to be implemented'''
    
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


'''
#TODO
- motor forward
- motor backward
- motor left
- motor right
- ping sensor
'''

while True:
    pass