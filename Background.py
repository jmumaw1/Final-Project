import pygame
import random
from Parameters import *

def draw_background(screen):
    sky = pygame.image.load("../Final-Project/assets/sprites/Additional_Sky.png").convert()
    water = pygame.image.load("../Final-Project/assets/sprites/Additional_Water.png").convert()
    lg_r = pygame.image.load("../Final-Project/assets/sprites/Water Reflect Big 04.png").convert()
    md_r = pygame.image.load("../Final-Project/assets/sprites/Water Reflect Medium 01.png").convert()
    sm_r = pygame.image.load("../Final-Project/assets/sprites/Water Reflect Small 04.png").convert()
    s_c = pygame.image.load("../Final-Project/assets/sprites/Small Cloud 2.png").convert()
    mid = pygame.image.load("../Final-Project/assets/sprites/BG Image.png").convert()

    sky.set_colorkey((0, 0, 0))
    water.set_colorkey((0, 0, 0))
    lg_r.set_colorkey((0, 0, 0))
    md_r.set_colorkey((0, 0, 0))
    sm_r.set_colorkey((0, 0, 0))
    s_c.set_colorkey((0, 0, 0))
    mid.set_colorkey((0, 0, 0))

    for x in range(0, WIDTH, s_t):
        for y in range(0, HEIGHT, s_t):
            screen.blit(sky, (x, y))

    for x in range(0, WIDTH, s_t):
        screen.blit(water, (x, HEIGHT-s_t))

    for x in range(0, WIDTH, s_t):
        screen.blit(mid, (x, HEIGHT/2))

    for _ in range(4):
        x = random.randint(0, WIDTH)
        screen.blit(lg_r, (x, HEIGHT - 50))

    for _ in range (3):
        x = random.randint(0, WIDTH)
        screen.blit(md_r, (x, HEIGHT - 125))

    for i in range (5):
        x = random.randint(0, WIDTH)
        screen.blit(sm_r, (x, HEIGHT - 225))

    for i in range (7):
        x = random.randint(0, WIDTH)
        screen.blit(s_c, (x, HEIGHT - 450))


