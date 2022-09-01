import time

import board

import pwmio


#P2 is S1 on Roboclaw
#Steps to reproduce!
'''
open basic micro studio, and update firmware to 4.2.1
have metrom4 9V battery VIN > roboclaw
Roboclaw plugged in and running on basic micro
Cpy running below code

Basic micro settings:
RC mode w/ 3 checks enabled, everything else default:

Mixing
Exponetial
MCU


'''

motor1 = pwmio.PWMOut(board.D2, frequency=50)
motor2 = pwmio.PWMOut(board.D3, frequency=50)

def servo_duty_cycle(pulse_ms, frequency=50):
    period_ms = 1.0 / frequency * 1000.0
    duty_cycle = int(pulse_ms / (period_ms / 65535.0))
    return duty_cycle


while True:

    motor1.duty_cycle = servo_duty_cycle(1.25)
    motor2.duty_cycle = servo_duty_cycle(1.25)
    time.sleep(2)
    print("forward")


    motor1.duty_cycle = servo_duty_cycle(1.75)
    motor2.duty_cycle = servo_duty_cycle(1.75)
    time.sleep(2)
    print("backward")