import curses
from random import randint  # Module that gives a random integer

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
    win.timeout(150 - (len(snake)) // 5 + len(snake) // 10 % 10)  # Increase speed

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
    # Get the current coordinates
    y = snake[0][0]  # The head
    x = snake[0][1]
    if key == curses.KEY_DOWN:  # okay, this isn't a tutorial. it's a code along... i'm slightly annoyed. #TrustTheProcess ;)
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        x += 1

    snake.insert(0, (y, x))

    # Check if the snake hit the border
    if y == 0:
        break
    if y == 19:
        break
    if x == 0:
        break
    if x == 59:
        break

    # Check if the snake hit itself
    if snake[0] in snake[1:]:
        break

    # Check if snake got to the food
    if snake[0] == food:
        # Eat the food
        score += 1
        # Make new food
        food = ()            # While food = empty tuple, make new food
        while food == ():
            food = (randint(1, 18), randint(1, 58))
            if food in snake:  # Don't let it generate new food that's inside the snake
                food = ()
        win.addch(food[0], food[1], '#')
    else:  # Move snake
        last = snake.pop()
        win.addch(last[0], last[1], ' ')

    win.addch(food[0], food[1], '#')
    win.addch(snake[0][0], snake[0][1], '*')

# SHUT THE GAME DOWN
curses.endwin()  # Destroys the window
print(f"Final score: {score}")
