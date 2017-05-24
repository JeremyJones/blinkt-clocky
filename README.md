# blinkt-clocky
An eight-light clock for Raspberry Pi using the Pimoroni Blinkt!


Help on module clocky:

NAME
    clocky - Blinkt-Clocky -- 8 light led clock for the Pimoroni Blinkt!

FILE
    /home/pi/Documents/blinkt-clocky/clocky.py

FUNCTIONS
    main()
        The Clocky light displays the hour range, the minute range, the
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
    
    sleep(...)
        sleep(seconds)
        
        Delay execution for a given number of seconds.  The argument may be
        a floating point number for subsecond precision.

DATA
    NUM_PIXELS = 8


