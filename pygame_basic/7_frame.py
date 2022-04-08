import pygame
############################################################# 
#default configure
pygame.init() #init pygame

#window size configure
screen_width = 480  #width
screen_height = 640    #height
screen = pygame.display.set_mode((screen_width, screen_height))

#screen title configure
pygame.display.set_caption("ShimBo Game") #name of game

#FPS
clock = pygame.time.Clock() 
################################################################

#1. User game initialization(background, game image, coordinates, fonts...etc)

running = True      #game is processing
while running:
    dt = clock.tick(30) #the number of frames in one sec


#2. event (keyboard, mouse...etc)
#event roop : to make the window stay in the screen

    print ("fps : " + str(clock.get_fps()))
    for event in pygame.event.get():    #what event occured
        if event.type == pygame.QUIT:  #window is closed
            running = False #game is over

#3. game character location

#4. collision

#5. get image on screen
        

    pygame.display.update() #keep drawing game image 


#game is ended
pygame.quit()
