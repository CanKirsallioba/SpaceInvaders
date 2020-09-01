import pygame
import os
import time
import random

#Load enemy ships
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))

#Load player controlled ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

#Load lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green"))

#Load background
BG = pygame.image.load(os.path.join("assets", "background-black.png"))

