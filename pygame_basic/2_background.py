import pygame


pygame.init() #init pygame

#window size configure
screen_width = 480   #width
screen_height = 640     #height
screen = pygame.display.set_mode((screen_width, screen_height))

#get backgroudn image
background = pygame.image.load( \
    "/Users/shimboyoung/Desktop/Python_Workspace/pygame_basic/colorado_pic.png")

#screen title configure
pygame.display.set_caption("ShimBo Game") #name of game


#event roop : to make the window stay in the screen
running = True      #game is processing
while running:
    for event in pygame.event.get():    #what event occured
        if event.type == pygame.QUIT:  #window is closed
            running = False #gaem is over

    screen.blit(background, (0, 0)) #image location, drawo image
    #screen.fill((0,0,255)) #screen color 
    pygame.display.update() #keep drawing game image 

#game is ended
pygame.quit()
