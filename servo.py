#!/usr/bin/env python3
#-- coding: utf-8 --
import RPi.GPIO as GPIO
import time

pwm = None

#Set function to calculate percent from angle
def angle_to_percent (angle) :
    if angle > 180 or angle < 0 :
        return False

    start = 4
    end = 12.5
    ratio = (end - start)/180 #Calcul ratio from angle to percent

    angle_as_percent = angle * ratio

    return start + angle_as_percent


def setup () :
    GPIO.setmode(GPIO.BOARD) #Use Board numerotation mode
    GPIO.setwarnings(False) #Disable warnings

    #Use pin 12 for PWM signal
    pwm_gpio = 11
    frequence = 50
    GPIO.setup(pwm_gpio, GPIO.OUT)
    pwm = GPIO.PWM(pwm_gpio, frequence)
    
    #Init at 0°
    pwm.start(angle_to_percent(0))
    time.sleep(1)

def enable_drs() :
    #Go at 45°
    pwm.ChangeDutyCycle(angle_to_percent(45))
    print("DRS Enabled")
    time.sleep(1)
    #Close GPIO & cleanup
    print("DRS Disabled")

def disable_drs() :
    #Back at 0°
    pwm.start(angle_to_percent(0))
    time.sleep(1)


def stop() : 
    pwm.stop()
    GPIO.cleanup()