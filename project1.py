#A normal bouncing ball.
import pygame  # The library that handles graphics and animation
import sys      # Lets us exit the program cleanly

# --- Setup ---
pygame.init()  # Start up pygame (always needed first)

WIDTH, HEIGHT = 800, 400             # Size of the window in pixels
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the window
pygame.display.set_caption("Bouncing Ball")        # Window title

clock = pygame.time.Clock()  # Used to control how fast the animation runs

# --- Ball properties ---
ball_x = 110    # Starting X position (horizontal)
ball_y = 120    # Starting Y position (vertical)
ball_radius = 27

speed_x = 10     # How many pixels to move right each frame
speed_y = 10    # How many pixels to move down each frame

BALL_COLOR  = (93, 202, 165)   # Teal  (Red, Green, Blue — values 0-255)
BG_COLOR    = (30, 30, 30)     # Dark background

# --- Main loop ---
# This loop runs ~60 times per second, redrawing everything each time
while True:

    # 1. Check for events (like the user closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # User clicked the X button
            pygame.quit()              # Shut down pygame
            sys.exit()                 # Exit the program

    # 2. Move the ball
    ball_x += speed_x   # Add speed to position each frame
    ball_y += speed_y

    # 3. Bounce off walls
    # If the ball's edge touches the right or left wall, flip horizontal direction
    if ball_x + ball_radius >= WIDTH or ball_x - ball_radius <= 0:
        speed_x = -speed_x   # Negative reverses direction!

    # If the ball's edge touches the top or bottom wall, flip vertical direction
    if ball_y + ball_radius >= HEIGHT or ball_y - ball_radius <= 0:
        speed_y = -speed_y

    # 4. Draw everything
    screen.fill(BG_COLOR)                                  # Wipe the screen clean
    pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), ball_radius)  # Draw ball

    pygame.display.flip()   # Show the newly drawn frame on screen
    clock.tick(60)          # Limit to 60 frames per second