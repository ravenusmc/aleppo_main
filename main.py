################################################
# BACKGROUND INFORMATION:
# This game was made by Mike Cuddy, Oct/Nov of 2016
#
#
# Enough cannot be said from the tutorials from Paul Craven at program arcade games.
# It is from that site that I was able to get code to build this game
# Paul Craven's site link which helped a lot with this game:
# http://programarcadegames.com/
# as well as from sentdex and his YouTube vidoes-both on his site and the New Boston.
# Those videos may be found at https://www.youtube.com/watch?v=Vom-Tuo0rcU&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO&index=7
#
# The platform game art came from Kenney.nl at http://opengameart.org/content/platformer-art-deluxe.


#Importing all of the files that will be used in this program.
import pygame
import random
import time
import levels
import support 

#initialization of pygame
pygame.init()

#Importing the player class.
from player import Player

#All of variables, which will be used for the music, will be set up here. 
bomb = pygame.image.load('bomb.png')
bomb_sound = pygame.mixer.Sound("bomb.wav")
explosion_sound = pygame.mixer.Sound("explosion.wav")
pygame.mixer.music.load("Grave_Matters.wav")
    
#This function will be what keeps track of the players score. It will display the bombs avoided message to the
#game screen as well as the number that have been avoided. 
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Bombs Avoided: " + str(count), True, support.green)
    support.screen.blit(text,(0,0))
    
#This function will create the bombs that will fall from the sky.
def things(thingx, thingy, thingw, thingh, color):
    support.screen.blit(bomb,(thingx, thingy))

#This is the main function to run the game. 
def main():
    
    #Here I start the music playing. The -1 means that the music will repeat
    #over and over again. However, the music will turn off if the player avoids 40
    #bombs. 
    pygame.mixer.music.play(-1)
    
    #When the player dies gameOver will be set to True.
    gameOver = False

    #These are the variables for the falling bombs. 
    thing_startx = random.randrange(0, support.S_WIDTH)
    #The bomb will start 300 pixels above the screen. 
    thing_starty = -300
    #This is the speed of the bomb. As each bomb falls this number will increase.
    thing_speed = 3
    thing_width = 128
    thing_height = 128

    #This variable keep tracks of the amount of bombs the player has avoided:
    dodged = 0

    #Create a player object from this line. 
    player = Player()

    #This will pull in all of the levels in the game.
    level_list = []
    level_list.append(levels.Level_01(player))

    #This sets the current level if I had more than one level. In this game
    #I only have 1 level, thus level_list has a value of 0 in it. 
    current_level = level_list[0]

    #This is what sets the player up in the current level.
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    #Setting up the dimensions for the player. 
    player.rect.x = 28
    player.rect.y = support.S_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    #With this variable being set to False, the below game loop
    #will keep on repeating until done is equal to True.
    done = False

    #The main game loop in the game. It will continue to run until the user quits or dies.
    while not done:
        #If gameOver is equal to True during the game loop then this
        #conditional statement will launch. 
        if gameOver == True:
            support.screen.fill(support.black)
            support.message_to_screen("You Died", support.red, -175, size="large")
            support.message_to_screen("It is estimated that over 400,000 People have died",
                              support.red, -100, size="small")
            support.message_to_screen("in the Syria Civil War",
                              support.red, -50, size="small")
            support.message_to_screen("Press p to play agian or Q to Quit", support.red, 0, size="medium")
            pygame.display.update()
            
        while gameOver == True:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    gameOver = False
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        done = True
                        gameOver = False
                    if event.key == pygame.K_p:
                        main()

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True 
            #These controls are what allow the player to move the character
            #on the screen. 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
                if event.key == pygame.K_p:
                    support.pause()
            #This code is what will stop the player from moving to the left or the right.
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        #The player is updated 
        active_sprite_list.update()

        #This line is where the non character elements get updated such as
        #the platforms that go up and down. 
        current_level.update()

        #This line is what will shift the screen to the left if the player
        #moves towards the right hand side.
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            current_level.shift_world(-diff)

        #This line is what will shift the screen to the right if the player
        #moves towards the left hand side.
        if player.rect.x <= 95:
            diff = 120 - player.rect.x
            player.rect.x = 120
            current_level.shift_world(diff)

        #These lines of code are what will cause a game over if the player
        #wonders to far to the left or to the right.
        current_position = player.rect.x + current_level.world_shift    
        if current_position < -4000 or current_position > 600:
            gameOver = True

        #Drawing objects to the game world should be made below this line.
        current_level.draw(support.screen)
        active_sprite_list.draw(support.screen)
        things_dodged(dodged)

        #logic for falling bombs
        things(thing_startx, thing_starty, thing_width, thing_height, support.green)
        thing_starty += thing_speed

        #This logic deals with the bombs falling from the sky.
        if thing_starty > support.S_HEIGHT:
            #This line plays the sound of the bombs falling
            pygame.mixer.Sound.play(bomb_sound)
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, support.S_WIDTH)
            #Increasing the score count of each bomb that passes the player
            dodged += 1
            #increasing the speed of the bombs as they pass the player.
            thing_speed += .5
            #I stop the music once dodged gets above 40 just to change the 'feeling'
            #of the game. 
            if dodged >= 40:
                pygame.mixer.music.stop()
                
        #This code will detect when the player has collided with a bomb. 
        if player.rect.y < thing_starty + thing_height and thing_starty + thing_height >= player.rect.y and thing_starty + thing_height <= 600:
            if player.rect.x > thing_startx and player.rect.x + 28 < thing_startx + thing_width:
                #If a player has collided with a bomb, the game is over. 
                gameOver = True
                pygame.mixer.Sound.play(explosion_sound)
                
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        
        #I set the timer to 60 seconds per frame. 
        support.clock.tick(60)

        #This will update the game screen at ever pass. 
        pygame.display.flip()

    pygame.quit()

#Here the functions, that start the game, are called.     
support.game_intro() #Calling game_intro function
support.background_information() #Calling background information function
main() #Calling main function
