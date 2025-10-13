import synscan

'''Goto example'''
smc=synscan.motors()
#Slow down long goto
smc.axis_set_long_goto_step_period(1, 3000); # AZ
smc.axis_set_long_goto_step_period(2, 3000); # ALT
#Synchronize mount actual position to (0,0)
smc.set_pos(0,0)
#Move forward and wait to finish
smc.goto(30,30,synchronous=True)
#Return to original position and exit without wait
smc.goto(0,0,synchronous=False)

