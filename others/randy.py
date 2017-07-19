import subprocess
from blinkt import *
import time
from datetime import datetime as dt
import re
from random import choice as pick


start_hour = dt.now().hour

while dt.now().hour == start_hour:
    load = float(re.sub(r'^.+?average: ([^,]+).+$', r'\1',
                        subprocess.check_output("uptime")))

    if load < 1:
        colour = 'white'
    elif load < 3:
        colour = 'blue'
    elif load < 6:
        colour = 'green'
    else:
        colour = 'red'

    sleep_time = 0.07
    
    clear()
    show()
    for p in range(NUM_PIXELS):
        if pick(range(2)) == 1:
            set_pixel(p, 40, 40, 40, 0.0323)
    show()
    time.sleep(sleep_time)
