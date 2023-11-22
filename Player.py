import pygame
import sys
import math
from Parameters import *

# Player properties
player_size = 200
player_x = 50  # Start the left side
player_y = HEIGHT - player_size
player_speed_y = 0
player_speed_x = 5

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.forward_image = pygame.image.load('../Final-Project/assets/sprites/test.png').convert()
        self.forward_image.set_colorkey((255, 255, 255))
        self.image = self.forward_image
        self.reverse_image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_speed = 0
        self.y_speed = 0

    def move_left(self):
        self.x_speed = -1 * player_speed_x
        self.image = self.reverse_image

    def move_right(self):
        self.x_speed = player_speed_x
        self.image = self.forward_image

    def stop(self):
        self.x_speed = 0

    def jump(self):
        self.y_speed = -JUMP_HEIGHT

    def Grav(self):
        self.y_speed += GRAVITY
        self.y_speed += player_speed_y
    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        if self.x > WIDTH-s_t:
            self.x = WIDTH-s_t
        if self.x < 0:
            self.x = 0
        if self.y > HEIGHT-s_t:
            self.y = HEIGHT-s_t
        if self.y < 0:
            self.y = 0

        self.rect.x = self.x
        self.rect.y = self.y


    def draw(self, surf):
        surf.blit(self.image, self.rect)
