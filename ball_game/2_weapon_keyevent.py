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
character_y_pos=screen_height-character_height-stage_height+10

#charcter movement
character_to_x =0

#character speed
character_speed=5

#create weapon
weapon=pygame.image.load(os.path.join(image_path,"armour.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

#can shoot several times at a time
weapons=[]

#weapon speed
weapon_speed=10

running = True      #game is processing
while running:
    dt = clock.tick(30) #the number of frames in one sec


#2. event (keyboard, mouse...etc)
#event roop : to make the window stay in the screen

    #print ("fps : " + str(clock.get_fps()))
    for event in pygame.event.get():    #what event occured
        if event.type == pygame.QUIT:  #window is closed
            running = False #game is over

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width/2) \
                    -(weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key ==pygame.K_RIGHT :
                character_to_x = 0
            elif event.key == pygame.K_SPACE:
                pass


#3. game character location
    character_x_pos += character_to_x
    if character_x_pos <0:
        character_x_pos=0
    elif character_x_pos > screen_width -character_width:
        character_x_pos=screen_width-character_width

#weapon loacation
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons] #put weapon up 

#weapon hit the top disappear
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons if w[1] > 0]
#4. collision

#5. get image on screen
    screen.blit(background,(0,0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon,(weapon_x_pos,weapon_y_pos))
    screen.blit(stage,(0,(screen_height-stage_height)))
    screen.blit(character,(character_x_pos,character_y_pos))
    
   

    pygame.display.update() #keep drawing game image 
#game is ended
pygame.quit()
