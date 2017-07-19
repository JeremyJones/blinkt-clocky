import subprocess
from blinkt import *
import time
from datetime import datetime as dt
import re

start_hour = dt.now().hour

while dt.now().hour == start_hour:
    clear()
    if bool(dt.now().second % 2):
        set_pixel(NUM_PIXELS-1, 40,40,40, 0.04)
    show()
    time.sleep(0.5)
