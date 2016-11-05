"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

Main module for platform scroller example.

From:
http://programarcadegames.com/python_examples/sprite_sheets/

Explanation video: http://youtu.be/czBDKWJqOao

Part of a series:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
http://programarcadegames.com/python_examples/sprite_sheets/

Game art from Kenney.nl:
http://opengameart.org/content/platformer-art-deluxe

"""

import pygame
import levels

pygame.init()
S_WIDTH  = 1000
S_HEIGHT = 800

# Colors
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

size = [S_WIDTH, S_HEIGHT]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("What is Aleppo")
clock = pygame.time.Clock()

from player import Player

#This function will render the correct placement of the text on the screen. 
def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
        
    return textSurface, textSurface.get_rect()
    
#This function will display text to the screen
def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (S_WIDTH / 2), (S_HEIGHT /2 ) + y_displace
    screen.blit(textSurf, textRect)
    
    
#This is the game intro function which will be what the user sees when the game
#first starts. 
def game_intro():
    
    intro = True
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                
        screen.fill(white)
        message_to_screen("What is Aleppo",
                          red,
                          -70,
                          size="large")
        message_to_screen("The goal of the game is to get through each level",
                          black,
                          0,
                          size="small")
        message_to_screen("In order to do this just follow the platforms...",
                          black,
                          40)
        message_to_screen("Press p to play or q to quit.",
                          black,
                          90)
        pygame.display.update()
        clock.tick(15)

#This function will provide background information about the city of Aleppo
#to the user.
def background_information():
    
    intro = True
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                
        screen.fill(white)
        message_to_screen("Background Information",
                          red,
                          -300,
                          size="large")
        message_to_screen("Aleppo is a city in Syria that is currently at the center of the Syrian civil war.",
                          black,
                          -230,
                          size="small")
        message_to_screen("It may have have been inhabitted as early as 8000 years ago. ",
                          black,
                          -200)
        message_to_screen("It was a city that had a population of over 2 million people.",
                          black,
                          -170)
        message_to_screen("The current population may be around 1.5 million",
                          black,
                          -140)
        message_to_screen("The city is located in North Western Syria, close to Turkey.",
                          black,
                          -100)
        message_to_screen("Many people consider Aleppo the worst hit city in Syria from the war.",
                          black,
                          -70)
        message_to_screen("The city, currently is splitt between the govenment-west and rebel-held east.",
                          black,
                          -40)
        message_to_screen("For a lot of its history, Aleppo was a 'cultural' location",
                          black,
                          -10)
        message_to_screen("It is the purpose of this game to bring some awareness to Aleppo",
                          black,
                          20)
        message_to_screen("That way, the player may hopefully never ask 'What is Aleppo'",
                          black,
                          50)
        message_to_screen("You may now press p to finally play or q to quit.",
                          black,
                          110)
        pygame.display.update()
        clock.tick(15)

def main():
    """ Main Program """


    # Create the player
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append(levels.Level_01(player))
    level_list.append(levels.Level_02(player))

    # Set the current level
    #This will change the current level that I am on. 
    current_level_no = 1
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 50
    player.rect.y = S_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    #Loop until the user clicks the close button.
    done = False

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            current_level.shift_world(diff)

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
    
game_intro()
background_information()
main()
