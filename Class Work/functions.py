# import libraries and modules
import pygame
import pygame as pg
from pygame.sprite import Sprite
from random import randint
from setting import *
from classes import *

# drawing grid function on display screen using pygame draw function
def draw_grid():
    for line in range(0, 20):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (WIDTH, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, HEIGHT))
    
# function for display text on screen
def draw_text(text, size, color, x, y):
        font_name = pg.font.match_font('PCF')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)
