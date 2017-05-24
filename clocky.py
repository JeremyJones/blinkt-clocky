"""
    Blinkt-Clocky -- 8 light led clock for the Pimoroni Blinkt!
"""
from datetime import datetime as dt
from time import sleep
from blinkt import clear, show, set_pixel, NUM_PIXELS
    
def main():
    """The Clocky light displays the hour range, the minute range, the
    second range, and a clock tick.

    To read the clock:

    The hours are represented by a blue bar with a bright end. The
    longer the bar, the later it is in the day. Each segment in the
    bar represents 3 hours.

    The minutes are represented by the 2nd light on the bar. A blue
    light is displayed when the minutes are between 0 and 15. A green
    light is displayed for minutes 16-30. A white light represents
    minutes 31-45 and a red light for minutes 46-59.

    The seconds are represented by the 1st light on the bar. A blue
    light is displayed when the seconds are between 0 and 15. A green
    light is displayed for seconds 16-30. A white light represents
    seconds 31-45 and a red light for seconds 46-59.

    If the last light on the bar is not already lit for another
    purpose, then it is used to display a pendulum of the clock,
    displaying a white light for the odd seconds within each minute.
    """
    while True:
        pixels = [None for i in range(NUM_PIXELS)]
        hour_now = dt.now().hour
        pixhr_now = int(hour_now/3)

        for p in range(pixhr_now): pixels[p] = 'H'
        pixels[pixhr_now-1] = '!'

        if hour_now > 2:
            second_pix, minute_pix = 0, 1
        else:
            second_pix = NUM_PIXELS - 1
            minute_pix = second_pix - 1

        pixels[minute_pix] = 'M'
        pixels[second_pix] = 'S'

        for i in range(len(pixels)):
            if pixels[i] == 'M': pixels[i] = "BGWR"[int(dt.now().minute /15)]
            elif pixels[i] == 'S': pixels[i] = "BGWR"[int(dt.now().second / 15)]
            elif pixels[i] == '!': pixels[i] = 1
            elif pixels[i] == 'H': pixels[i] = "B"
        
        clear()
        for i in filter(lambda _: bool(pixels[_]), range(len(pixels))):
            if type(pixels[i]) is int and pixels[i] == 1: set_pixel(i, 100, 0, 100, 0.1)
            elif pixels[i] == 'R': set_pixel(i, 200, 0, 0, 0.033)
            elif pixels[i] == 'G': set_pixel(i, 0, 200, 0, 0.033)
            elif pixels[i] == 'B': set_pixel(i, 0, 0, 200, 0.033)
            elif pixels[i] == 'W': set_pixel(i, 200, 200, 200, 0.033)

        if second_pix == 0 and pixels[-1] is None: # set second flash if that last pixel is free and it's normal mode
            if bool(dt.now().second % 2): set_pixel(len(pixels)-1, 20, 20, 20, 0.033)
        
        show()
        sleep(0.5)

if __name__ == "__main__":
    main()
