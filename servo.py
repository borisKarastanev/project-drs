#!/usr/bin/env python3
#-- coding: utf-8 --
try:
    import RPi.GPIO as GPIO

except ImportError as error:
    print(f"Supported only on Raspberry Pi {error}")
    raise error


import time
import config


def setup():
    GPIO.setmode(GPIO.BOARD) #Use Board numerotation mode
    GPIO.setwarnings(False) #Disable warnings

    #Use pin 12 for PWM signal
    pwm_gpio = config.servos['right_servo_pin']
    frequency = config.servos['frequency']
    GPIO.setup(pwm_gpio, GPIO.OUT)
    pwm = GPIO.PWM(pwm_gpio, frequency)
    
    #Init at 0°
    disable_drs(pwm)
    return pwm

#Set function to calculate percent from angle
def angle_to_percent (angle):
    if angle > 180 or angle < 0 :
        raise ValueError("Please provide a valid angle between 0 - 180")

    start = 4
    end = 12.5
    ratio = (end - start)/180 #Calcul ratio from angle to percent

    angle_as_percent = angle * ratio

    return start + angle_as_percent


def enable_drs(pwm, angle=config.drs_angles['medium']):
    #Go at 45°
    pwm.ChangeDutyCycle(angle_to_percent(angle))
    print("DRS Enabled")
    time.sleep(1)

def disable_drs(pwm):
    #Back at 0°
    pwm.start(angle_to_percent(config.drs_angles['disabled']))
    print("DRS Disabled")
    time.sleep(1)


def stop(pwm):
     #Close GPIO & cleanup 
    pwm.stop()
    GPIO.cleanup()