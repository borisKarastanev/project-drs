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
        
        #Init at 45°
        self.enable_drs()

    def setup(self):
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


    def disable_drs(self):
        #Go at 45°
        
        self._pwm['left_pwm'].ChangeDutyCycle(self._angle_to_percent(config.left_servo_drs_angles['disabled']))
        self._pwm['right_pwm'].ChangeDutyCycle(self._angle_to_percent(config.right_servo_drs_angles['disabled']))

        print("DRS Disabled")
        

    def enable_drs(self):
        #Back at 0°
        self._pwm['left_pwm'].start(self._angle_to_percent(config.left_servo_drs_angles['enabled']))
        self._pwm['right_pwm'].start(self._angle_to_percent(config.right_servo_drs_angles['enabled']))

        print("DRS Enabled")


    def stop(self):
        #Close GPIO & cleanup 
        self._pwm['left_pwm'].stop()
        self._pwm['right_pwm'].stop()
        GPIO.cleanup()