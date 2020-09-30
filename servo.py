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

        #Use pin 12 for PWM signal
        pwm_gpio = config.servos['right_servo_pin']
        frequency = config.servos['frequency']
        GPIO.setup(pwm_gpio, GPIO.OUT)
        pwm = GPIO.PWM(pwm_gpio, frequency)
        return pwm


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
        self._pwm.ChangeDutyCycle(self._angle_to_percent(angle))
        print("DRS Enabled")
        time.sleep(1)

    def disable_drs(self):
        #Back at 0°
        self._pwm.start(self._angle_to_percent(config.drs_angles['disabled']))
        print("DRS Disabled")
        time.sleep(1)


    def stop(self):
        #Close GPIO & cleanup 
        self._pwm.stop()
        GPIO.cleanup()