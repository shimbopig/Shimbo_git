import pygame
import os
############################################################# 
#default configure
pygame.init() #init pygame

#window size configure
screen_width = 640  #width
screen_height = 480    #height
screen = pygame.display.set_mode((screen_width, screen_height))

#screen title configure
pygame.display.set_caption("Shimbo BALL Game") #name of game

#FPS
clock = pygame.time.Clock() 
################################################################

#1. User game initialization(background, game image, coordinates, fonts...etc)

current_path = os.path.dirname(__file__) #give current file path 
image_path = os.path.join(current_path, "images") #give images folder

#create background
background = pygame.image.load(os.path.join(image_path, "background.png")) #get background png

#create stage
stage=pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size=stage.get_rect().size
stage_height=stage_size[1] #height

#create character
character=pygame.image.load(os.path.join(image_path,"character.png"))
character_size=character.get_rect().size
character_width=character_size[0]
character_height=character_size[1]
character_x_pos=screen_width/2-(character_width/2)
character_y_pos=screen_height-character_height




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
    screen.blit(background,(0,0))
    screen.blit(stage,(0,(screen_height-stage_height)))
    screen.blit(character,(character_x_pos,character_y_pos))
    pygame.display.update() #keep drawing game image 
#game is ended
pygame.quit()
