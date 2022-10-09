# snake_game.py - A simple snake game

import pygame
import sys
import random
import time

check_errors = pygame.init()
if check_errors[1] > 0:
    continue
else:
    print("Ok")

# Play surface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption("Snake game!")

# Colors
red = pygame.Color(255, 0, 0)  # gameover
green = pygame.Color(0, 255, 0)  # snake
