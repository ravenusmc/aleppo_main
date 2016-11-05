#This file is where the player class will be coded.

import pygame

import constants

from platforms import MovingPlatform
from spritesheet_functions import SpriteSheet

class Player(pygame.sprite.Sprite):
    
    #Setting variables for the speed of the player.
    change_x = 0
    change_y = 0

    #These two lists are what will hold the frames for the chacacter to make
    #the character appear as if they are walking. 
    walking_frames_l = []
    walking_frames_r = []

    #Setting the initial direction for which way the player will face.
    direction = "R"

    # List of sprites we can bump against
    #level = None

    #Initialization the character
    def __init__(self):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        #Setting up the sprite image for the character. 
        sprite_sheet = SpriteSheet("boy_2.png")
        image = sprite_sheet.get_image(8, 210, 28, 210)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(40, 210, 28, 210)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(70, 210, 28, 210)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(103, 210, 28, 210)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(136, 210, 28, 210)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(166, 210, 28, 210)
        self.walking_frames_r.append(image)

        image = sprite_sheet.get_image(8, 210, 28, 210)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(40, 210, 28, 210)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(70, 210, 28, 210)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(103, 210, 28, 210)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(136, 210, 28, 210)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(166, 210, 28, 210)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

    #This method will be what will move the player.
    def update(self):
        
        #The calc_grav() function is what will be used to calculate gravity
        #During game play.
        self.calc_grav()

        #This code here is what will move the player left and right
        self.rect.x += self.change_x
        #This is what shifts the world based on the player location
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        #This code here will change the y value of the player location.
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

    def calc_grav(self):
        #The code in here will calculate the effect of gravity.
        if self.change_y == 0:
            self.change_y = 1
        else:
            #This changes the gravity level in the game. A lower value makes you jump higher.
            #A higher value makes your jumps smaller.
            self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -10

    #Changing the direction and speed of the player movement with the below methods.
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -8
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 8
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
