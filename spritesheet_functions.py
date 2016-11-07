#This file is what will allow me to pull in individual sprite sheets.

import pygame

import constants

#This class is used to grab the sprite sheets.
class SpriteSheet(object):

    # This points to our sprite sheet image
    #sprite_sheet = None

    def __init__(self, file_name):

        #Load and convert the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()

    #This function will allow us to get a single image out of a large
    #sprite sheet. In order to do this, use a program like Microsoft Paint.
    #Find the upper left hand corner of your image and get the x,y coordinates
    #of that location. Then get the image width and the height. 
    def get_image(self, x, y, width, height):
        
        #This line creates the new image. It will recieve the image that
        #is copied from the sprite sheet. 
        image = pygame.Surface([width, height]).convert()

        #This sets the copied image, from above to the image that was cut out.
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        #Setting the background color to black. 
        image.set_colorkey(constants.BLACK)

        #return image
        return image
