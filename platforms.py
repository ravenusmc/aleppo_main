#The code in this file will be dealing with the platforms in the game.
import pygame

from spritesheet_functions import SpriteSheet

#These are the platforms that will be used in the game. The first two numbers
#are the x,y location of the image on the sprite sheet. The third number is the
#width and finally, the last number, is the height. 
STONE_PLATFORM_LEFT   = (432, 720, 70, 40)
STONE_PLATFORM_MIDDLE = (648, 648, 70, 40)
STONE_PLATFORM_RIGHT  = (792, 648, 70, 40)

#Creating a platform class. 
class Platform(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet_data):
        
        pygame.sprite.Sprite.__init__(self)
        #Getting the tiles from the sprite sheet and saving it as a
        #variable sprite_sheet. 
        sprite_sheet = SpriteSheet("tiles_spritesheet.png")
        # Grab the image for this platform. The [0] represents the x value,
        #the [1] is the y value, the [2] is the width and finally, the [3]
        #is the height.
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()

#Setting up a class for the moving platform
class MovingPlatform(Platform):
    
    change_x = 0
    change_y = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

##    level = None
##    player = None

    def update(self):
        # Move left/right
        self.rect.x += self.change_x

        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # If we are moving right, set our right side
            # to the left side of the item we hit
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.player.rect.left = self.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # Reset our position based on the top/bottom of the object.
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        # Check the boundaries and see if we need to reverse
        # direction.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
