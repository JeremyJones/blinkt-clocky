import subprocess
from blinkt import *
import time
from datetime import datetime as dt
import re

start_hour = dt.now().hour

while dt.now().hour == start_hour:
    idle = float(re.sub(r'^.+? (\S+) id, .+$', r'\1',
                        subprocess.\
                        check_output("/usr/bin/top -n 1")))
                        #check_output("top -n 1 | head | grep Cpu")))

    clear()
    idle_lights = int(idle / 20.0)

    for p in range(idle_lights):
        set_pixel(p, 0,100,0, 0.1)

    if bool(dt.now().second % 2):
        set_pixel(NUM_PIXELS-1, 40,40,40, 0.2)
        
    show()
    time.sleep(0.5)
