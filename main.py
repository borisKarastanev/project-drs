#!/usr/bin/env python3
#-- coding: utf-8 --

import servo

try:
    servo.setup()
    servo.enable_drs()
    servo.disable_drs()
    servo.stop()
except:
    print("DRS Failed")