import pygame
  
class test:
    # initializing the constructor
    pygame.init()
  
    # opens up a window
    screen = pygame.display.set_mode((720,720))

    # stores the width of the
    # screen into a variable
    width = screen.get_width()
  
    # stores the height of the
    # screen into a variable
    height = screen.get_height()
  
    # defining a font
    smallfont = pygame.font.SysFont('Corbel',35)
  
    # rendering a text written in
    # this font
    text = smallfont.render('quit' , True , (255,255,255))
  
    while True:
      
        for event in pygame.event.get():
          
            if event.type == pygame.QUIT:
                pygame.quit()
              
            #checks if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
              
            #if the mouse is clicked on the
            # button the game is terminated
                if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                    pygame.quit()
                  
        # fills the screen with a color
        screen.fill((60,25,60))
      
        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()
      
        # if mouse is hovered on a button it
        # changes to lighter shade 
        if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
            pygame.draw.rect(screen,(170,170,170),[width/2,height/2,140,40])
          
        else:
            pygame.draw.rect(screen,(100,100,100),[width/2,height/2,140,40])
      
        # superimposing the text onto our button
        screen.blit(text , (width/2+50,height/2))
      
        # updates the frames of the game
        pygame.display.update()