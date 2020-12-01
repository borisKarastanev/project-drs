#!/usr/bin/env python3
#-- coding: utf-8 --

from servo import Servo

try:
    servo = Servo()
    servo.enable_drs()
    servo.disable_drs()
    servo.stop()

except Exception as error:
    print("DRS Failed", error)
    
