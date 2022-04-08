import pygame
import random 


pygame.init() #init pygame

#window
screen_width=480
screen_height=640
screen= pygame.display.set_mode((screen_width,screen_height))

#get background image
background = pygame.image.load("/Users/shimboyoung/Desktop/Python_Workspace/poop_game/colorado_pic.png")

#get character image
character = pygame.image.load("/Users/shimboyoung/Desktop/Python_Workspace/poop_game/character.png")
character_size=character.get_rect().size    #image size
character_width=character_size[0]
character_height=character_size[1]
character_x_pos=screen_width/2-(character_width/2) #character's first location
character_y_pos=screen_height-(character_height)

#location
to_x=0
to_y=0

#accelation
accelation=10
poop_speed=10

#get poop image
poop = pygame.image.load("/Users/shimboyoung/Desktop/Python_Workspace/poop_game/poop.png")
poop_size= character.get_rect().size
poop_width= character_size[0]
poop_height= character_size[1]
poop_x_pos= random.randint(0, (screen_width-poop_width))
poop_y_pos= poop_height

#screen title
pygame.display.set_caption("Poop_Game")

#FPS
clock =pygame.time.Clock()

#Font
game_font = pygame.font.Font(None,40)

#total_score
total_score=0

#total_time
total_time=30

#starting_time
start_ticks=pygame.time.get_ticks()

#event roop

running= True   #game is running
while running:
    screen.blit(background,(0,0))
    dt=clock.tick(30)

    #print ("fps : " + str(clock.get_fps()))
    for event in pygame.event.get():    #what event occured
        if event.type == pygame.QUIT:  #window is closed
            running = False #gaem is over

        if event.type == pygame.KEYDOWN: #if keyboard is pressed
            if event.key==pygame.K_LEFT:    # left keyboard
                to_x -= accelation
                
               
            elif event.key==pygame.K_RIGHT:     #right Keyboard
                to_x += accelation

        if event.type == pygame.KEYUP:  #not pushing keyboard
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    
    character_x_pos+=to_x
    screen.blit(poop,(poop_x_pos,poop_y_pos))
    
    poop_y_pos+=poop_speed
    

    #charater width boundary
    if character_x_pos <0 :
        character_x_pos=0
    elif character_x_pos > (screen_width-character_width):
        character_x_pos = screen_width- character_width
    #charater height boundary
    if character_y_pos <0 :
        character_y_pos = 0
    elif character_y_pos > screen_height-character_height:
        character_y_pos = screen_height-character_height
        
    #poop ground approach
    if poop_y_pos > screen_height:
        poop_y_pos =0
        poop_x_pos = random.randint(0,(screen_width-poop_width))
    #collsion 
    character_rect=character.get_rect()
    character_rect.left=character_x_pos
    character_rect.top=character_y_pos

    poop_rect=poop.get_rect()
    poop_rect.left=poop_x_pos
    poop_rect.top=poop_y_pos

    #collosion check
    if character_rect.colliderect(poop_rect):
        running = False

    #draw on screen
    
    screen.blit(character, (character_x_pos,character_y_pos))
    

    #elapsed time 
    elapsed_time = (pygame.time.get_ticks() - start_ticks)/1000
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    
    screen.blit(timer, (10,10))
    #if time<0 = quit game
    if total_time - elapsed_time <=0:
        print("time out")
        running = False



    pygame.display.update() #keep drawing game image 

#wait before end the game
pygame.time.dealay(2000) #delay 2seconds before quit the game

#game is ended
pygame.quit()


