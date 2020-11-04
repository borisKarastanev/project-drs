#!/usr/bin/env python3
#-- coding: utf-8 --
try:
    import RPi.GPIO as GPIO

except ImportError as error:
    print(f"Supported only on Raspberry Pi {error}")
    raise error


import time
import config

class Servo:
    def __init__(self):
        self._pwm = self.setup()
        
        #Init at 0°
        self.disable_drs()

    def setup(self):
        GPIO.setmode(GPIO.BOARD) #Use Board numerotation mode
        GPIO.setwarnings(False) #Disable warnings

        frequency = config.servos['frequency']

        #Use pin 11 for right servo motor
        right_servo_gpio = config.servos['right_servo_pin']
        GPIO.setup(right_servo_gpio, GPIO.OUT)

        left_servo_gpio = config.servos['left_servo_pin']
        GPIO.setup(left_servo_gpio, GPIO.OUT)

        right_pwm = GPIO.PWM(right_servo_gpio, frequency)
        left_pwm = GPIO.PWM(left_servo_gpio, frequency)

        return dict(
            left_pwm = left_pwm,
            right_pwm = right_pwm
        )


    #Set function to calculate percent from angle
    def _angle_to_percent (self, angle):
        if angle > 180 or angle < 0 :
            raise ValueError("Please provide a valid angle between 0 - 180")

        start = 4
        end = 12.5
        ratio = (end - start)/180

        angle_as_percent = angle * ratio

        return start + angle_as_percent


    def enable_drs(self, angle=config.drs_angles['medium']):
        #Go at 45°
        
        self._pwm['left_pwm'].ChangeDutyCycle(self._angle_to_percent(angle))
        self._pwm['right_pwm'].ChangeDutyCycle(self._angle_to_percent(angle))

        print("DRS Enabled")
        time.sleep(1)

    def disable_drs(self):
        #Back at 0°
        self._pwm['left_pwm'].start(self._angle_to_percent(config.drs_angles['disabled']))
        self._pwm['right_pwm'].start(self._angle_to_percent(config.drs_angles['disabled']))

        print("DRS Disabled")
        time.sleep(1)


    def stop(self):
        #Close GPIO & cleanup 
        self._pwm['left_pwm'].stop()
        self._pwm['right_pwm'].stop()
        GPIO.cleanup()