#importing the files that are needed for this file.
import pygame
import constants
#platforms needs to be imported in order to create the platforms that I will be
#using in the level
import platforms

#Creating a level class which will hold the 'game world'
class Level():

    #This variable will determine how far the level has been scrolled left
    #to right.
    world_shift = 0

    #Initializing method
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    #The update method will update everything on the level.
    def update(self):
        self.platform_list.update()

    #This method will draw everything in the level
    def draw(self, screen):
        
        #This will draw/change the background. 
        screen.fill(constants.BLUE)
        screen.blit(self.background,(self.world_shift // 3,0))

        #Draw all sprites to the game world
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    #This method will shift the world when the user moves to the left or right.
    def shift_world(self, shift_x):
        
        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

#This class will create the level. It will really be focusing on creating
#all of the platforms in the level. The code in this class is quite massive.
#It is because this is basically what is making all of the obstacles, platforms,
#for the game. 
class Level_01(Level):
    
   #This class is what will create the level for the game. 
    def __init__(self, player):

        #Calling the parent constructor.
        Level.__init__(self, player)

        #I load up my background image in the below line.
        self.background = pygame.image.load("Aleppo_One.png").convert()
        #This line sets a transparent color for the background.
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -500
        
        # Adding moving platforms for the player. There are quite a lot
        #added here which I did soley to get a better understanding of how
        #to add these platforms
        #Platform 1
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_LEFT)
        block.rect.x = 300
        block.rect.y = 300
        block.boundary_top = 200
        block.boundary_bottom = 400
        block.change_y = -8
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        #Platform 2
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 500
        block.rect.y = 500
        block.boundary_top = 400
        block.boundary_bottom = 650
        block.change_y = -5
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        #Platform 3
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 600
        block.rect.y = 600
        block.boundary_top = 500
        block.boundary_bottom = 700
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        #Platform 4
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_LEFT)
        block.rect.x = 900
        block.rect.y = 700
        block.boundary_top = 300
        block.boundary_bottom = 800
        block.change_y = -3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        #Platform 5
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1400
        block.rect.y = 700
        block.boundary_top = 300
        block.boundary_bottom = 800
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        #Platform 6
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 1700
        block.rect.y = 700
        block.boundary_top = 300
        block.boundary_bottom = 800
        block.change_y = -6
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        #Platform 7
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 2300
        block.rect.y = 700
        block.boundary_top = 200
        block.boundary_bottom = 800
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        #Platform 8
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 2800
        block.rect.y = 600
        block.boundary_top = 500
        block.boundary_bottom = 800
        block.change_y = -5
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        #Platform 9
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 3000
        block.rect.y = 600
        block.boundary_top = 300
        block.boundary_bottom = 800
        block.change_y = -5
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        #Platform 10
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 3400
        block.rect.y = 600
        block.boundary_top = 300
        block.boundary_bottom = 800
        block.change_y = -5
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        #These platforms prevent the user from going to far to the right.
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 4200
        block.rect.y = 550
        block.boundary_top = 550
        block.boundary_bottom = 600
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 4200
        block.rect.y = 500
        block.boundary_top = 500
        block.boundary_bottom = 550
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 4200
        block.rect.y = 450
        block.boundary_top = 450
        block.boundary_bottom = 500
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 4200
        block.rect.y = 400
        block.boundary_top = 400
        block.boundary_bottom = 450
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 4200
        block.rect.y = 350
        block.boundary_top = 350
        block.boundary_bottom = 400
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        #These platforms prevent the user from going to far to the Left.
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = -50
        block.rect.y = 550
        block.boundary_top = 550
        block.boundary_bottom = 600
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = -50
        block.rect.y = 500
        block.boundary_top = 500
        block.boundary_bottom = 550
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = -50
        block.rect.y = 450
        block.boundary_top = 450
        block.boundary_bottom = 500
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = -50
        block.rect.y = 400
        block.boundary_top = 400
        block.boundary_bottom = 450
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = -50
        block.rect.y = 350
        block.boundary_top = 350
        block.boundary_bottom = 400
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        #These platforms form a wall that the player must get through to progress
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 800
        block.rect.y = 550
        block.boundary_top = 550
        block.boundary_bottom = 600
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 800
        block.rect.y = 500
        block.boundary_top = 500
        block.boundary_bottom = 550
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 800
        block.rect.y = 450
        block.boundary_top = 450
        block.boundary_bottom = 500
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 800
        block.rect.y = 400
        block.boundary_top = 400
        block.boundary_bottom = 450
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 800
        block.rect.y = 350
        block.boundary_top = 350
        block.boundary_bottom = 400
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        
        #These platforms form a wall that the player must get through to progress
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 1200
        block.rect.y = 550
        block.boundary_top = 550
        block.boundary_bottom = 600
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 1200
        block.rect.y = 500
        block.boundary_top = 500
        block.boundary_bottom = 550
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 1200
        block.rect.y = 450
        block.boundary_top = 450
        block.boundary_bottom = 500
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 1200
        block.rect.y = 400
        block.boundary_top = 400
        block.boundary_bottom = 450
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 1200
        block.rect.y = 350
        block.boundary_top = 350
        block.boundary_bottom = 400
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        #These platforms form a wall that the player must get through to progress
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 2000
        block.rect.y = 550
        block.boundary_top = 550
        block.boundary_bottom = 600
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 2000
        block.rect.y = 500
        block.boundary_top = 500
        block.boundary_bottom = 550
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 2000
        block.rect.y = 450
        block.boundary_top = 450
        block.boundary_bottom = 500
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 2000
        block.rect.y = 400
        block.boundary_top = 400
        block.boundary_bottom = 450
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 2000
        block.rect.y = 350
        block.boundary_top = 350
        block.boundary_bottom = 400
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        
        #These platforms form a wall that the player must get through to progress
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 3200
        block.rect.y = 550
        block.boundary_top = 550
        block.boundary_bottom = 600
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 3200
        block.rect.y = 500
        block.boundary_top = 500
        block.boundary_bottom = 550
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 3200
        block.rect.y = 450
        block.boundary_top = 450
        block.boundary_bottom = 500
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 3200
        block.rect.y = 400
        block.boundary_top = 400
        block.boundary_bottom = 450
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 3200
        block.rect.y = 350
        block.boundary_top = 350
        block.boundary_bottom = 400
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 3200
        block.rect.y = 250
        block.boundary_top = 250
        block.boundary_bottom = 350
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_RIGHT)
        block.rect.x = 3200
        block.rect.y = 200
        block.boundary_top = 200
        block.boundary_bottom = 250
        block.change_y = 0
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


