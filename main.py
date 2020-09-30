#!/usr/bin/env python3
#-- coding: utf-8 --

from servo import Servo

try:
    # pwm = servo.setup()
    # servo.enable_drs(pwm)
    # servo.disable_drs(pwm)
    # servo.stop(pwm)
    servo = Servo()
    servo.enable_drs()
    servo.disable_drs()
    servo.stop()

except Exception as error:
    print("DRS Failed", error)