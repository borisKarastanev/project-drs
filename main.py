#!/usr/bin/env python3
#-- coding: utf-8 --

import servo

try:
    pwm = servo.setup()
    servo.enable_drs(pwm)
    servo.disable_drs(pwm)
    servo.stop(pwm)

except Exception as error:
    print("DRS Failed", error)