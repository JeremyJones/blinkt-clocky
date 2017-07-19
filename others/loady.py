import subprocess
from blinkt import *
import time
from datetime import datetime as dt
import re

start_hour = dt.now().hour

while dt.now().hour == start_hour:
    load = float(re.sub(r'^.+?average: ([^,]+).+$', r'\1',
                        subprocess.check_output("uptime")))

    clear()
    if load < 0.5:
        set_all(0,100,0,0.2)
        show()
    else:
        lit_up = int(load)%8
        set_pixel(lit_up, 100, 0, 0, 0.2)
        for p in range(NUM_PIXELS):
            if p != lit_up:
                set_pixel(p,0,0,100,0.2)
                
        show()

    time.sleep(1)
