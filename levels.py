import pygame

import constants
import platforms

class Level():

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None
##    enemy_list = None

    # Background image
    #background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    #level_limit = -1000

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    # Update everything on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        #This will draw/change the background. 
        screen.fill(constants.BLUE)
        screen.blit(self.background,(self.world_shift // 3,0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        #For enemies in the game. 
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

# Create platforms for the level
class Level_01(Level):
   #This class is what will create the level for the game. 
    def __init__(self, player):

        # Call the parent constructor
        Level.__init__(self, player)

        #I load up my background image in the below line.
        self.background = pygame.image.load("Aleppo_One.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -500
        
        # Adding moving platforms for the player. There are quite a lot
        #added here which I did soley to get a better understanding of how
        #to add these platforms
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_LEFT)
        block.rect.x = 300
        block.rect.y = 300
        block.boundary_top = 300
        block.boundary_bottom = 600
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 500
        block.rect.y = 500
        block.boundary_top = 400
        block.boundary_bottom = 650
        block.change_y = -3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 700
        block.rect.y = 700
        block.boundary_top = 500
        block.boundary_bottom = 800
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_LEFT)
        block.rect.x = 900
        block.rect.y = 700
        block.boundary_top = 500
        block.boundary_bottom = 800
        block.change_y = -3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1400
        block.rect.y = 700
        block.boundary_top = 500
        block.boundary_bottom = 800
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 1700
        block.rect.y = 700
        block.boundary_top = 500
        block.boundary_bottom = 800
        block.change_y = -3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_LEFT)
        block.rect.x = 2000
        block.rect.y = 700
        block.boundary_top = 500
        block.boundary_bottom = 800
        block.change_y = -3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 2500
        block.rect.y = 700
        block.boundary_top = 500
        block.boundary_bottom = 800
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 2800
        block.rect.y = 700
        block.boundary_top = 500
        block.boundary_bottom = 800
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


