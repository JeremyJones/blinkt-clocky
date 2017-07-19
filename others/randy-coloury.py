import subprocess
from blinkt import *
import time
from datetime import datetime as dt
import re
from random import choice as pick

start_hour = dt.now().hour
sleep_time = 0.2


def my_set_pixel(pixnum, r, g, b, brightness, offset):
    rgbs = [[255,0,0],
            [255,66,0],
            [255,255,0],
            [0,255,0],
            [0,0,255],
            [75,0,130],
            [238,130,238],
            [0,0,0]]

    secondpixnum = ((pixnum + offset) % NUM_PIXELS)

    set_pixel(secondpixnum,
              int(rgbs[pixnum][0]/1.5),
              int(rgbs[pixnum][1]/1.5),
              int(rgbs[pixnum][2]/1.5),
              brightness)


def main():
    while dt.now().hour == start_hour:
    
        clear()
        show()
        offset = dt.utcnow().second % NUM_PIXELS
        
        for p in range(NUM_PIXELS):
            if (not p) or pick(range(10)):
                my_set_pixel(p, 40, 40, 40, 0.0323, offset)
        show()
        time.sleep(sleep_time)
        

if __name__ == '__main__':
    main()
