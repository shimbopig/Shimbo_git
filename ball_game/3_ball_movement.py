from re import I
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

#creat ball
ball_images =[
    pygame.image.load(os.path.join(image_path,"bigball.png")),
    pygame.image.load(os.path.join(image_path,"middleball.png")),
    pygame.image.load(os.path.join(image_path,"little_small.png")),
    pygame.image.load(os.path.join(image_path,"small_ball.png"))]

#according to the ball size speed get different
ball_speed_y = [-18, -15, -12, -9]  #ball speed

#balls
balls =[]

#first ball create
balls.append({
    "pos_x" : 50, # x of ball
    "pos_y" : 50, # y of ball
    "img_idx" :0, #index of ball
    "to_x":3, # movement of x , -3 : left, +3 : right
    "to_y": -6, # movement of y
    "init_spd_y":ball_speed_y[0]}) #initial y speed


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

#ball location
for ball_idx, ball_val in enumerate(balls): #enumerate: get index and value
    ball_pos_x = ball_val["pos_x"]
    ball_pos_y = ball_val["pos_y"]
    ball_img_idx = ball_val["img_idx"]

    ball_size = ball_images[ball_img_idx].get_rect().size
    ball_width = ball_size[0]
    ball_height = ball_size[1]

    #when ball hit the side wall it bounce
    if ball_pos_x <= 0 or ball_pos_x > screen_width -ball_width:
        ball_val["to_x"]=ball_val["to_x"]* -1

    #when ball hit the top down wall it bounce
    if ball_pos_y >= screen_height - stage_height - ball_height:
        ball_val["to_y"]= ball_val["init_spd_y"]
    else:
        ball_val["to_y"]+=0.5
    
    ball_val["pos_x"]+=ball_val["to_x"]
    ball_val["pos_x"]+=ball_val["to_y"]

#4. collision

#5. get image on screen
    screen.blit(background,(0,0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon,(weapon_x_pos,weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val ["img_idx"]
        screen.blit(ball_images[ball_img_idx],(ball_pos_x,ball_pos_y))

    screen.blit(stage,(0,(screen_height-stage_height)))
    screen.blit(character,(character_x_pos,character_y_pos))
    
   

    pygame.display.update() #keep drawing game image 
#game is ended
pygame.quit()
