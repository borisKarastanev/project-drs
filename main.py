#!/usr/bin/env python3
#-- coding: utf-8 --
import RPi.GPIO as GPIO
import time
import servo

try:
    pwm = servo.setup()
    servo.enable_drs(pwm, 45)
    servo.disable_drs(pwm)
    servo.stop(pwm)

except:
    print("DRS Failed")