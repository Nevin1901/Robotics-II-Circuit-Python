import time
import board
import pwmio

'''
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

#4 second pause once the m4 is initialized. 
time.sleep(4)

#Main motor move forward, stop, backwards, stop
motor1.duty_cycle = servo_duty_cycle(min_speed)
motor2.duty_cycle = servo_duty_cycle(min_speed)
print("Full forward")
time.sleep(2)

motor1.duty_cycle = servo_duty_cycle(stop)
motor2.duty_cycle = servo_duty_cycle(stop)
print("stop")
time.sleep(2)

motor1.duty_cycle = servo_duty_cycle(max_speed)
motor2.duty_cycle = servo_duty_cycle(max_speed)
print("Full backward")
time.sleep(2)

motor1.duty_cycle = servo_duty_cycle(stop)
motor2.duty_cycle = servo_duty_cycle(stop)
print("stop")
time.sleep(2)
