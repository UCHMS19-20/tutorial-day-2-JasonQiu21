import sys
import pygame
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

# start running pygame
pygame.init()

width, height = 1920, 1080
# speed is a list because values need to be able to change
speed = [1, 1]
# colors are tuples because values don't change
black = (0, 0, 0)
white = (255, 255, 255)

# Create a display. The size must be a tuple providing width and height
screen = pygame.display.set_mode( (width, height) )

# Load an image
ball = pygame.image.load(f"{dir_path}/img/just_accept_it.jpg")
ballrect = ball.get_rect()

while True:
    #wait 16 ms - that makes it just over 60 FPS
    pygame.time.wait(16)
    # loop through every event in the event queue
    for event in pygame.event.get():
        # if the QUIT event happens, exit the program
        if event.type == pygame.QUIT:
            sys.exit()
    
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] *= -1
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] *= -1

    # Fill the screen with white
    screen.fill(white)
    # Draw the ball with the size and location specified by ballrect
    screen.blit(ball, ballrect)
    # Update the display
    pygame.display.flip()