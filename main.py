import curses

# setup window
curses.initscr()  # init screen
win = curses.newwin(20, 60, 0, 0)  # (lines, columns, y, x) ... usually
                                    # it's (x,y) for coordinates
win.keypad(1)  # Lets the program know we want to use the arrow keys
curses.noecho()  # Don't want
