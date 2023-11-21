import pygame
import sys
import math
from Parameters import *

# Player properties
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT // 2 - player_size // 2
player_speed_y = 0
is_jumping = False
