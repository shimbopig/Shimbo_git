import pygame


pygame.init() #init pygame

#window size configure
screen_width = 480  #width
screen_height = 640    #height
screen = pygame.display.set_mode((screen_width, screen_height))

#get backgroudn image
background = pygame.image.load( \
    "/Users/shimboyoung/Desktop/Python_Workspace/pygame_basic/colorado_pic.png")

#get character
character = pygame.image.load("/Users/shimboyoung/Desktop/Python_Workspace/pygame_basic/character.png")
character_size = character.get_rect().size #get image size
character_width = character_size[0]    #width of character
character_height = character_size[1]    #height of character
character_x_pos = screen_width/2 - (character_width/2)     #locat in middle of the screen
character_y_pos = screen_height - character_height    #bottom of the screen

#location
to_x = 0 
to_y = 0

#accelation
accelation=5

#enemy character
enemy = pygame.image.load("/Users/shimboyoung/Desktop/Python_Workspace/pygame_basic/enemy.png")
enemy_size = character.get_rect().size #get image size
enemy_width = character_size[0]    #width of character
enemy_height = character_size[1]    #height of character
enemy_x_pos = screen_width/2 - (enemy_width/2)     #locat in middle of the screen
enemy_y_pos = (screen_height/2) - enemy_height    #bottom of the screen

#screen title configure
pygame.display.set_caption("ShimBo Game") #name of game

#FPS
clock = pygame.time.Clock() 

#event roop : to make the window stay in the screen
running = True      #game is processing
while running:
    dt = clock.tick(30) #the number of frames in one sec

    print ("fps : " + str(clock.get_fps()))
    for event in pygame.event.get():    #what event occured
        if event.type == pygame.QUIT:  #window is closed
            running = False #gaem is over

        if event.type == pygame.KEYDOWN: #if keyboard is pressed
            if event.key==pygame.K_LEFT:    # left keyboard
                to_x -= accelation
            elif event.key==pygame.K_RIGHT:     #right Keyboard
                to_x += accelation
            elif event.key==pygame.K_UP:    #up keyboard
                to_y -= accelation
            elif event.key==pygame.K_DOWN:  #down keyboard
                to_y += accelation

        if event.type == pygame.KEYUP:  #not pushing keyboard
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x 
    character_y_pos += to_y 

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
        
    #collision rect
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top =  character_y_pos 

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    #collision check
    if character_rect.colliderect(enemy_rect):
        print("collide!")
        running = False
        

    screen.blit(background, (0, 0)) #image location, drawo image
    #screen.fill((0,0,255)) #screen color 
    screen.blit(character, (character_x_pos, character_y_pos)) #draw character
    screen.blit(enemy, (enemy_x_pos,enemy_y_pos))   #draw enemy 
    pygame.display.update() #keep drawing game image 

#game is ended
pygame.quit()
