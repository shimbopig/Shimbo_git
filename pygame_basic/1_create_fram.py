import pygame


pygame.init() #init pygame

#window size configure
screen_width = 480   #width
screen_height = 640     #height
pygame.display.set_mode((screen_width, screen_height))

#screen title configure
pygame.display.set_caption("ShimBo Game") #name of game


#event roop : to make the window stay in the screen
running = True      #game is processing
while running:
    for event in pygame.event.get():    #what event occured
        if event.type == pygame.QUIT:  #window is closed
            running = False #gaem is over
 
#game is ended
pygame.quit()
