import time
import board
import pwmio

'''
DEBUG Notes, feel free to ignore these quotes
open basic micro studio, and update firmware to 4.2.1
have metrom4 9V+ battery VIN > roboclaw
Roboclaw plugged in and running on basic micro
Cpy running below code

Basic micro settings:
RC mode w/ 3 checks enabled, everything else default:

Mixing
Exponetial
MCU

Button mode 1 (RC)
Option 4 (Tank Style)
Option 5 (Differential Steering Style)


'''

#init motors as pwm objects
motor1 = pwmio.PWMOut(board.D2, frequency=50)
motor2 = pwmio.PWMOut(board.D3, frequency=50)


def servo_duty_cycle(pulse_ms, frequency=50):
    period_ms = 1.0 / frequency * 1000.0
    duty_cycle = int(pulse_ms / (period_ms / 65535.0))
    return duty_cycle

#Define Min/Max/Stop commands
min_speed = 1 #full forward
max_speed = 2 #full backward
stop = 1.5 #needs to be calibrated by motor. 

while True:

    motor1.duty_cycle = servo_duty_cycle(min_speed)
    motor2.duty_cycle = servo_duty_cycle(min_speed)
    print("Full forward")
    time.sleep(2)
    


    motor1.duty_cycle = servo_duty_cycle(max_speed)
    motor2.duty_cycle = servo_duty_cycle(max_speed)
    print("Full backward")
    time.sleep(2)
    

    motor1.duty_cycle = servo_duty_cycle(stop)
    motor2.duty_cycle = servo_duty_cycle(stop)
    print("stop")
    time.sleep(2)