#!/usr/bin/env python3
import synscan
import time

'''Goto example'''
def run():
  smc=synscan.motors()
  smc._set_T1_preset(1, 3000); # AZ
  smc.axis_start_motion(1)
  time.sleep(1)
  smc.axis_stop_motion(1)

run()
