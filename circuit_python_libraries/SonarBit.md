# Using a Ping Sensor in CircuitPython

This tutorial will teach you how to use a ping sensor (in our case, a "SonarBit" branded ping sensor) on a M4 board. 

Start by copying the sonarbit.py code above onto your code.py file on your M4. 

## Code Explanation

Firstly, we import all revelant libraries. Math will be important for later. 

```
""" Sonarbit Distance Program."""

import time
import board
import digitalio
from math import floor
```

Now, we define a new function for getting our distance. Unlike an ultrasonic sensor used on a hummingbird:bit, that had 1 pin for send, and 1 pin for recieve, the ping sensor uses the *same pin* for both send and recieve. This requires some tricky programming to get working in CircuitPython, 

```
def sonar(pin):
    ''' Get a ping reading from 5cm>568cm from the Elecfreaks Ping Sensor. Trigger & Echo are on the 'same pin'. 
    pin = the pin with the ping sensor
    returns: Distance in cm between 0 & 568

    Note: If object is <5cm away, it will register either 0 or 568cm away. 
    Note: Introduce a 0.1sec delay when taking sensor readings in CircuitPython, else the code will stop parsing. 
    
    '''
    
    usleep = lambda x: x/1000000

    pin.direction = digitalio.Direction.OUTPUT

    #send trigger signal
    pin.value = 0
    usleep(2)
    pin.value = 1
    usleep(10)
    pin.value = 0

    #recieve echo signal
    pin.direction = digitalio.Direction.INPUT
    while pin.value == 0:
        start_time = time.monotonic_ns()

    while pin.value == 1:
        end_time = time.monotonic_ns()

    #If an object is too close, start_time will never be assigned because pin.value will never equal 0, causing a variable assignment error & crash. 
    try:
        # Distance is defined as time/2 (there and back) * speed of sound 34000 cm/s
        distance = floor((end_time - start_time) * 34000/2/1000000000)
    except:
        print("object too close")
        distance = 0
    
    return distance


pin = digitalio.DigitalInOut(board.D2)
while True:
    print("the object is " + str(sonar(pin)) + " cm away")
    time.sleep(0.5)
```
