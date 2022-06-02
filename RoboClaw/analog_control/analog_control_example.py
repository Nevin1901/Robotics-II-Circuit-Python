# Analog control motor via controller
# Roboclaw controller, Mode 3-1
# 1V = stop. 0V = Max backwards, 2V = Mac forwards

"""CircuitPython Analog Out example"""
import board
import time
from analogio import AnalogOut

analog_out = AnalogOut(board.A0)
print("start")

while True:
    # Count up from 0 to 65535, with 64 increment
    for i in range(0, 65535, 64):
        analog_out.value = i
        time.sleep(.1)
        print(i)
