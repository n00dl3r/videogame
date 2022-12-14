# import libraries and modules
import pygame
import pygame as pg
from pygame.sprite import Sprite
from random import randint
from setting import *
from functions import *

# Classes
class World():
    def __init__(self, data):
        # list to store the data from the construction of the world
        self.tile_list = []    
        # load images
        ice_img = pygame.image.load(os.path.join(game_folder, 'ice_tile.png')).convert_alpha()
        # this loop will load in a img then scale that by the tile size and make a rectangle from that
        row_count = 0
        for row in data:
            # varable allow for for loop know where to put tile from the world_data information
            col_count = 0 
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(ice_img, (tile_size, tile_size))
                    # gives imported image convert it into rectangle object to store its information used later for collision 
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    # save both img_rect and the img in a touple
                    tile = (img, img_rect)
                    # use append function from python to add to list
                    self.tile_list.append(tile)
                if tile == 2:
                    spike = Spikes(col_count * tile_size, row_count * tile_size)
                    spike_group.add(spike)
                if tile == 3:
                    door = Door(col_count * tile_size, row_count * tile_size)
                    door_group.add(door)
                col_count += 1
            row_count += 1
    # draw method
    def draw(self):
        for tile in self.tile_list:
            # to draw the img import    
            screen.blit(tile[0], tile[1])
            # draw rectangle around the block sprite
            # pygame.draw.rect(screen, WHITE, tile[1], 2)
class Spikes(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # load images
        img = pygame.image.load(os.path.join(game_folder, 'spike.png'))
        self.image = pygame.transform.scale(img, (tile_size, tile_size))
        # gives imported image convert it into rectangle object to store its information used later for collision 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Door(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # load images
        img = pygame.image.load(os.path.join(game_folder, 'door.png'))
        self.image = pygame.transform.scale(img, (tile_size, tile_size))
        # gives imported image convert it into rectangle object to store its information used later for collision 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Player:
    def __init__(self, x ,y):
        # list of img assets
        self.images_right = []
        self.images_left = []
        self.index = 0
        # use self.counter to track speed of player animation
        self.counter = 0
        # for loop to load multiple imgs
        for num in range(1,5):
            img_right = pygame.image.load(os.path.join(game_folder, f'penguin_sprite_0{num}.png')).convert_alpha()
            img_right = pygame.transform.scale(img_right,(tile_size,tile_size -5))
            # flip the img right for left using pygame 
            img_left = pygame.transform.flip(img_right, True, False)
            # to not overide use append function. add to list
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        # use the first img from the images_right list whe first loaded in
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.animation_time = 0.5
        self.in_air = True
        self.health = 100 
        self.dead = False  
    def update(self):
        dx = 0
        dy = 0
        self.dead = False
        walk_cooldown = 1

        # movement inputs based on key presses
        key = pygame.key.get_pressed()
        if (key[pygame.K_SPACE] or key[pygame.K_w]) and self.jumped == False and self.in_air == False:
            self.vel_y = -15
            self.jumped = True
        if (key[pygame.K_SPACE] == False or key[pygame.K_w] == False):
            self.jumped = False
        if key[pygame.K_a]:
            dx -= 5
            # counter +1 only if movement keys are pressed 
            self.counter +=1
            self.direction = -1
        if key[pygame.K_d]:
            dx += 5
            # counter +1 only if movement keys are pressed 
            self.counter +=1
            self.direction = 1
        # if statement to reset the image's animation if keys not pressed
        if key[pygame.K_a] == False and key[pygame.K_d]== False:
            self.counter = 0 
            self.index = 0
            if self.direction == 1:
                self.images = self.images_right[self.index]
            if self.direction == -1:
                self.images = self.images_left[self.index]

        # animatio update. if statement to slow down the animation
        self.index += self.animation_time
        # if statement to make sure that the sprite resets once it exceeds the length of the list
        if self.index >= len(self.images_right):
                self.index = 0
        if self.direction == 1:
            self.image = self.images_right[int(self.index)]
        if self.direction == -1:
            self.image = self.images_left[int(self.index)]

        # add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        # state that in_air true
        self.in_air = True
        # check colision using for loop to check collsion with tiles on world map
        for tile in game_world.tile_list:
            # check for colsion along the x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            # check for colsion along the y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # check is below the ground when jumping
                if self.vel_y < 0:
                    dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                # check is above the ground when falling
                elif self.vel_y >= 0:
                    dy = tile[1].top - self.rect.bottom
                    self.vel_y = 0
                    self.in_air = False
        # if player sprite collide spike group sprites -1 to player health
        if pygame.sprite.spritecollide(self, spike_group, False):
            self.health -= 1
        if self.health <= 0:
            self.dead = True
        # if player sprite collide door sprites kill player sprite
        if pygame.sprite.spritecollide(self, door_group, False):
            self.dead = True
        # update player cordinates
        self.rect.x += dx
        self.rect.y +=dy

        # Make sure player not fall through Screen
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            dy = 0
        if self.rect.top < 0:
            self.rect.top = 0
            dy = 0
        
        # draw player no screen
        screen.blit(self.image, self.rect)
        
        # draw rectangle around the player sprite
        # pygame.draw.rect(screen, WHITE, self.rect, 2)
    def display(self):
        if self.dead == False:
            self.update()
        # if player colldie with door group kill player sprite and display YOU WIN
        elif pygame.sprite.spritecollide(self, door_group, False):
            self.dead = True
            draw_text("YOU  WIN", 50, BLUE, WIDTH / 2, 320)

# instence of the world class
game_world = World(level_map)
# instence of player
player = Player(50, HEIGHT - 130)