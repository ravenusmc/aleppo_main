################################################
# BACKGROUND INFORMATION:
# This game was made by Mike Cuddy, Oct/Nov of 2016
#
#
# Enough cannot be said from the tutorials from Paul Craven at program arcade games. His site link is below.
# It is from that site that I was able to get code to build this game
# Paul Craven's site link which helped a lot with this game: http://programarcadegames.com/python_examples/f.php?file=move_sprite_keyboard_smooth.py
# as well as from sentdex and his YouTube vidoes-both on his site and the New Boston.
# Those videos may be found at https://www.youtube.com/watch?v=Vom-Tuo0rcU&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO&index=7
#
# The platform game art came from Kenney.nl at http://opengameart.org/content/platformer-art-deluxe.


#Importing all of the files that will be used in this program.
import pygame
import random
import time
import levels

#initialization of pygame
pygame.init()

#Importing the player class.
from player import Player

#All of variables, which will be used for the music, will be set up here. 
bomb = pygame.image.load('bomb.png')
bomb_sound = pygame.mixer.Sound("bomb.wav")
explosion_sound = pygame.mixer.Sound("explosion.wav")
pygame.mixer.music.load("Grave_Matters.wav")

#The screen dimensions for the game will be declared here.
S_WIDTH  = 1000
S_HEIGHT = 800

# Colors that will be used will be declared here. 
light_red = (200,0,0)
red = (255,0,0)
light_blue = (0,0,200)
blue = (0,0,255)
light_green = (0,200,0)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)

#The variables for the different size fonts are declared here. 
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

#Setting up the screen display, title for the display and pygame clock.
size = [S_WIDTH, S_HEIGHT]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("What is Aleppo")
clock = pygame.time.Clock()

#This function will render the correct placement of the text on the screen. The
#last variable size will determine the size of the font on the screen. 
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
    #This line will center the text on the screen.
    textRect.center = (S_WIDTH / 2), (S_HEIGHT /2 ) + y_displace
    #This line will actually display the text on the screen. 
    screen.blit(textSurf, textRect)

#This function will alert the user if they die. 
def crash():
    #The music is stopped when the player 'dies'
    pygame.mixer.music.stop()
    #The 'you died' message is then displayed from the message_to_screen
    #function.
    message_to_screen("You Died",
                          red,
                          -70,
                          size="large")

#This function will alert the user if they went out of bounds. It is similar
#to the crash function except that the player is told that they went out of
#bounds and the game is now over. 
def out_of_bounds():
    pygame.mixer.music.stop()
    message_to_screen("You went out of bounds!",
                          red,
                          -70,
                          size="large")
    
#This function will be what keeps track of the players score. It will display the bombs avoided message to the
#game screen as well as the number that have been avoided. 
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Bombs Avoided: " + str(count), True, green)
    screen.blit(text,(0,0))
    
#This function will create the bombs that will fall from the sky.
def things(thingx, thingy, thingw, thingh, color):
    screen.blit(bomb,(thingx, thingy))
   
#This is the game intro function which will be what the user sees when the game
#first starts. 
def game_intro():
    
    intro = True
    #This while loop will display the welcoming message. When the player hits
    #either p or q, the function will exit and move on to the next screen. 
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
        #making the background color of the screen white.         
        screen.fill(white)
        #Display the title screen messages to the user. 
        message_to_screen("What is Aleppo",
                          red,
                          -200,
                          size="large")
        message_to_screen("The goal of the game is to simply avoid the falling bombs",
                          black,
                          -100,
                          size="small")
        message_to_screen("Each bomb that passes you gives you one point",
                          black,
                          -50)
        message_to_screen("The moving platforms may help or slow you down!",
                          black,
                          0)
        message_to_screen("Do not wander to far to the left or right or you will die",
                          black,
                          50)
        message_to_screen("Press p to play, p to pause, in the game, and q to quit.",
                          black,
                          180)
        pygame.display.update()
        clock.tick(15)

#This function will provide background information about the city of Aleppo
#to the user. It will display one of two messages depending on which random number is drawn.
def background_information():

    #The intro variable is set to true so that the while loop may execute.
    intro = True

    #in order to generate different information on the screen, I use a random number that
    #will display either one set of information of another. 
    rand_number = random.randint(0,100)

    #The loop constantly refreshes the screen awaiting for players commands. When the user tells
    #the computer to do something, intro is False and the screen moves on. 
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
        #Displays first set of messages if the random number is below 50. 
        if rand_number < 50:
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
            message_to_screen("The city, currently is split between the govenment-west and rebel-held east.",
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
        #Displays second set of messages if the random number is 50 or above. 
        elif rand_number >= 50:
            message_to_screen("Aleppo is a city in Syria that in 2011 was its largest city.",
                              black,
                              -230,
                              size="small")
            message_to_screen("In 2011, Aleppo was estimated to have a population of about 2.5 million. ",
                              black,
                              -200)
            message_to_screen("Although the Syrian Civil War started in 2011, Aleppo did not feel it until 2012.",
                              black,
                              -170)
            message_to_screen("The current population may be around 1.5 million",
                              black,
                              -140)
            message_to_screen("It is widely believed that civilians get purposely targeted in the city.",
                              black,
                              -100)
            message_to_screen("One of the worst weapons of use in the city are the barrel bombs.",
                              black,
                              -70)
            message_to_screen("The Syrian govenment drops these bombs out of helicopters.",
                              black,
                              -40)
            message_to_screen("The bombs have killed thousands and caused wide spread destruction.",
                              black,
                              -10)
            message_to_screen("It is the purpose of this game to bring some awareness to Aleppo",
                              black,
                              20)
            message_to_screen("That way, the player may hopefully never ask 'What is Aleppo'",
                              black,
                              50)
            
        message_to_screen("You may now press p to finally PLAY or q to QUIT.",
                          black,
                          110)
        pygame.display.update()
        clock.tick(15)

#This function will create the pause menu. Each time that the player pauses the screen, they will also
#see a random fact about the current situation in Aleppo, Syria. 
def pause():

    #The paused variable is set to true so when the pause screen is called, the game
    #goes into a while loop.
    paused = True
    
    #In order to generate different information on the screen, I use a random number that
    #will display either one set of facts or another. 
    number = random.randint(0,100)
    
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                #If c is pressed the user will exit the pause screen and continue
                #playing.
                if event.key == pygame.K_c:
                    paused = False
                #If q is pressed the game will exit and then close. 
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        #The background of the pause screen is filled with white so that the player
        #is not able to see where the next bomb will be coming from. 
        screen.fill(white)
        message_to_screen("Paused",
                          red,
                          -200,
                          size="large")
        #First message 
        if number <= 25:
            message_to_screen("The Syrian Civil War has led to almost 5 million refugees.",
                          red,
                          -90,
                          size="small")
        #Second message
        elif number > 25 and number <= 50:
            message_to_screen("Over 1 million Syrians have requested asylum in other countries.",
                          red,
                          -90,
                          size="small")
        #Third message
        elif number > 50 and number <= 75:
            message_to_screen("Over 6 million people have been internally displayed by the war.",
                          red,
                          -90,
                          size="small")
        #Fourth message
        elif number > 75 and number <= 100:
            message_to_screen("It is the worst exodus since the Rwandan genocide 20 years ago.",
                          red,
                          -90,
                          size="small")
        message_to_screen("Press c to play or q to quit.",
                          black,
                          150)

        
        pygame.display.update()
        clock.tick(15)

#This is the main function to run the game. 
def main():
    
    #Here I start the music playing. The -1 means that the music will repeat
    #over and over again. However, the music will turn off if the player avoids 40
    #bombs. 
    pygame.mixer.music.play(-1)
    
    #When the player dies gameOver will be set to True.
    gameOver = False

    #These are the variables for the falling bombs. 
    thing_startx = random.randrange(0, S_WIDTH)
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
    player.rect.y = S_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    #With this variable being set to False, the below game loop
    #will keep on repeating until done is equal to True.
    done = False

    #The main game loop in the game. It will continue to run until the user quits or dies.
    while not done:
        #If gameOver is equal to True during the game loop then this
        #conditional statement will launch. 
        if gameOver == True:
            screen.fill(black)
            message_to_screen("You Died", red, -175, size="large")
            message_to_screen("It is estimated that over 400,000 People have died",
                              red, -100, size="small")
            message_to_screen("in the Syria Civil War",
                              red, -50, size="small")
            message_to_screen("Press p to play agian or Q to Quit", red, 0, size="medium")
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
                    pause()
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
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        things_dodged(dodged)

        #logic for falling bombs
        things(thing_startx, thing_starty, thing_width, thing_height, green)
        thing_starty += thing_speed

        #This logic deals with the bombs falling from the sky.
        if thing_starty > S_HEIGHT:
            pygame.mixer.Sound.play(bomb_sound)
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, S_WIDTH)
            #Increasing the score count of each bomb that passes the player
            dodged += 1
            #increasing the speed of the bombs as they pass the player.
            thing_speed += .5
            #I stop the music once dodged gets above 40 just to change the 'feeling'
            #of the game. 
            if dodged >= 40:
                pygame.mixer.music.stop()
                
        #This code will detect when the player has collided with a bomb. 
        if player.rect.y < thing_starty + thing_height and thing_starty + thing_height >= player.rect.y and thing_starty + thing_height <= 800:
            if player.rect.x > thing_startx and player.rect.x + 28 < thing_startx + thing_width:
                #If a player has collided with a bomb, the game is over. 
                gameOver = True
                pygame.mixer.Sound.play(explosion_sound)
                
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        
        #I set the timer to 60 seconds per frame. 
        clock.tick(60)

        #This will update the game screen at ever pass. 
        pygame.display.flip()

    pygame.quit()

#Here the functions, that start the game, are called.     
game_intro() #Calling game_intro function
background_information() #Calling background information function
main() #Calling main function
