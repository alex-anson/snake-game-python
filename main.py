import curses

# SETUP WINDOW
curses.initscr()  # init screen
win = curses.newwin(20, 60, 0, 0)  # (lines, columns, y, x) ... usually
                                    # it's (x,y) for coordinates
win.keypad(1)  # Lets the program know we want to use the arrow keys
curses.noecho()  # Don't want other keypresses to show up in the terminal
curses.curs_set(0)  # Hide the cursor
win.border(0)  # Draw a border
win.nodelay(1)  # (no delay)  docs say: "if flag is True, getch()
                # will be non-blocking"   getch = get character


# SNAKE & FOOD (Coordinates)
snake = [(4, 10), (4, 9), (4, 8)]
food = (10, 20)

# GAME LOGIC
score = 0

# Game should run unless user presses escape key.
ESC = 27  # Define a constant with uppercase
key = curses.KEY_RIGHT  # Starting by moving the snake to the right

while key != ESC:
    win.addstr(0, 2, 'Score: ' + str(score) + ' ')  # Add a string
                            # (3rd argument) at 0,2 (y,x). (no idea why
                            # there's a space after the score variable)
    win.timeout(150 - (len(snake)) // 5 + len(snake) // 10 % 120)  # Increase speed

    prev_key = key
    event = win.getch()  # Wait for the next user input
    key = event if event != -1 else prev_key
    # ^ "if event (user input) is not -1 (he referenced the nodelay method but
    # i've no idea what he's talking about), otherwise, use the previous key,
    # continuing in the same direction"

    # Check if it's one of the arrow keys
    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key = prev_key

    # Calculate the next coordinates for the snake, starting with the head
    y = snake[0][0]

    for s in snake:
        win.addch(s[0], s[1], '*')  # (y, x, character to use)

    win.addch(food[0], food[1], '#')

# SHUT THE GAME DOWN
curses.endwin()  # Destroys the window
print(f"Final score: {score}")
