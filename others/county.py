import subprocess
from blinkt import *
import time
from datetime import datetime as dt
import re

start_hour = dt.now().hour

while dt.now().hour == start_hour:
    clear()
    
    load = float(re.sub(r'^.+?average: ([^,]+).+$', r'\1',
                        subprocess.check_output("uptime")))

    sleep_time = 0.07 + (load * 0.01)

    print "sleep time is {}".format(sleep_time)
    
    for p in range(NUM_PIXELS):
        set_pixel(p, 40, 40, 40, 0.05)
        show()
        time.sleep(sleep_time)

    #for p in range(NUM_PIXELS-1,0,-1):
    #for p in range(NUM_PIXELS,0,-1):
    for p in range(NUM_PIXELS):
        #set_pixel(p-1, 0,0,0, 0.0)
        set_pixel(p, 0,0,0, 0.0)
        show()
        time.sleep(sleep_time)
