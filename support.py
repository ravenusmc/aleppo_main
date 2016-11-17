#This file holds all of the support functions that are used in the game. 

#importing files which are needed in order for this file to work.
import pygame
import random

#initialization of pygame
pygame.init()

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
    
#This function will display text to the screen
def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    #This line will center the text on the screen.
    textRect.center = (S_WIDTH / 2), (S_HEIGHT /2 ) + y_displace
    #This line will actually display the text on the screen. 
    screen.blit(textSurf, textRect)

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
