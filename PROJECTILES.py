import pygame
import sys
import math
from Parameters import *

# Projectile properties
projectiles = []
class Projectile:
    def __init__(self, x, y, angle, color):
        self.x = x
        self.y = y
        self.angle = angle
        self.color = color

    def move(self):
        self.x += PROJECTILE_SPEED * math.cos(self.angle)
        self.y += PROJECTILE_SPEED * math.sin(self.angle)

