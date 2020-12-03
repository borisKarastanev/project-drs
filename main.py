#!/usr/bin/env python3
#-- coding: utf-8 --

from servo import Servo
from gpiozero import Button

button = Button(27, pull_up=False, hold_time=0)
    

try:
    servo = Servo()
    button.when_held = servo.enable_drs
    button.when_released = servo.disable_drs

except Exception as error:
    print("DRS Failed", error)
    
