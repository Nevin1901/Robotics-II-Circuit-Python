import time
import board
import pwmio
from adafruit_motor import servo

'''
Button mode 1 (RC)
Option 4 (Tank Style)
Option 5 (Differential Steering Style)
'''

#init motors as pwm objects
motor1 = pwmio.PWMOut(board.D2, frequency=50)
motor2 = pwmio.PWMOut(board.D3, frequency=50)

#init servo main arm up/down control
pwm = pwmio.PWMOut(board.D4, frequency=50)
main_arm = servo.ContinuousServo(pwm)
#+ is down, - is Up
#8sec to top of arm, 7 sec down



#servo gripper arms
#d5 left
#d6 right
pwm1 = pwmio.PWMOut(board.D5, frequency=50)
left_servo = servo.Servo(pwm1)
pwm2 = pwmio.PWMOut(board.D6, frequency=50)
right_servo = servo.Servo(pwm2)

def servo_duty_cycle(pulse_ms, frequency=50):
    period_ms = 1.0 / frequency * 1000.0
    duty_cycle = int(pulse_ms / (period_ms / 65535.0))
    return duty_cycle

#Define Min/Max/Stop commands
min_speed = 1.0 #full forward
max_speed = 2.0 #full backward
stop = 1.5 #needs to be calibrated by motor.

def motor_test():
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

def arm_full_up():
    main_arm.throttle = -1
    time.sleep(12.2)

def arm_full_return():
    main_arm.throttle = 1
    time.sleep(12.2)

def grab():
    pass
#arm_full_up()
#arm_full_return()

while True:
    time.sleep(5)
    motor_test()

