

""" Sonarbit Distance Program
Credit to student Z. for assistance in making this code more efficient. 
"""

import time
import board
import digitalio
from math import floor

def sonar(pin, prev_distance = 570, sleep = True):
    ''' Get a ping reading from 5cm>568cm from the Elecfreaks Pin Sensor. Trigger & Echo are on the 'same pin'. 
    pin = accepts pin argument with the ping sensor attached
    prev_distance: accepts an int between 0>568. intended to catch false 568 high readings if <5cm to sensor
        default value is only given for initial run, after this initial call you should input a previous distance
    sleep = Accepts boolean. Intended to introduce a 0.05ms sleep inbetween sensor readings, else program crashes from too many calls to the sensor. 
    returns: Distance in cm between 0 & 568
    

    Note: Introduce a 0.05sec delay when taking sensor readings in CircuitPython, else the code will stop parsing. 
    
    '''
    
    usleep = lambda x: x/1000000

    pin.direction = digitalio.Direction.OUTPUT

    #send trigger signal
    pin.value = 0
    time.sleep(usleep(2))
    pin.value = 1
    time.sleep(usleep(10))
    pin.value = 0

    #recieve echo signal
    pin.direction = digitalio.Direction.INPUT
    original_time = time.monotonic_ns() 

    while pin.value == 0:
        start_time = time.monotonic_ns()
        #this stops an infinite loop sometimes caused by rapid movements in front of the sensor. I am unsure of why
        #this happens occassionally, but this "safety check" stops this from happening
        if (start_time - original_time > 50000000):
            break

    while pin.value == 1:
        end_time = time.monotonic_ns()

    #If an object is too close, start_time will never be assigned because pin.value will never equal 0, causing a variable assignment error & crash. 
    try:
        # Distance is defined as time/2 (there and back) * speed of sound 34000 cm/s
        distance = floor((end_time - start_time) * 34000/2/1000000000)
    except:
        distance = 0

    #check if user has entered a previous distance
    if prev_distance >= 570:
        pass
    else:
        #if our previous distance was close, and suddenly we register a VERY FAR object, we clearly are reading a false high 568cm, return the previously read value. 
        if prev_distance < 15 and distance > 150:
            distance = prev_dist
    
    #you may take this out if necesssary and you are doing other time based functions on your code. If you are not, leave this in otherwise you will send out signals too quickly for what the ping sensor can send/recieve from. 
    if sleep:
        time.sleep(0.05)
    return distance


pin = digitalio.DigitalInOut(board.D2)
while True:
    distance = sonar(pin)
    print("the object is " + str(distance) + " cm away")
    time.sleep(0.05)

