
from time import sleep #from time  impotts the sleep library
import pygame #imports pygame library

pygame.init()#intaling py game

def main():
    
    # Set up the drawing window
    screen = pygame.display.set_mode([500, 500])
    
    pygame.display.set_caption("cool shop")
    
    # Fill the background with white
    screen.fill((255, 255, 255))
    screen.fill("white")
    
    
    #drawing
    pygame.draw.rect(screen, "black", [150, 150, 200 , 200]) #Draw a black rectangle in the chanter
    pygame.draw.circle(screen, "red", [255 , 255] , 3) # Draw a red blue circle in the center
    pygame.draw.polygon(screen,"blue", ((0, 0), (0, 50), (25, 75), (50, 50), (50, 0))) # Draw a blue polygon in corner
   
    #add text
    font = pygame.font.SysFont(None, 20)
    text_put = font.render('sound', True, "white")
    screen.blit(text_put, (5, 5))
    
    #music 
    soundObj = pygame.mixer.Sound('punch.wav')

    
    
    #change now to gray
    change = True 
    while True:
        
        for event in pygame.event.get(): #alll events
            
            if event.type == pygame.QUIT: #quit
                pass
            
            #mouse chek
            #pos[0] זה מיקום האופקי של העבר
            #pos[1] זה מיקום האנכי של העבר
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                
                if 150 < pos[0] < 350 and 150 < pos[1] < 350:    
                    pass
                
                #sounds
                if 0 < pos[0] < 50 and 0 < pos[1] < 75:
                    pass
                
                ##done this evry time
                #AD here a commend to do every time yoy change thomthink
                print(pos)
            
            
        #bring all the chges you make in grafich to the screen
        pygame.display.flip()
       

    # Done! Time to quit.
    pygame.quit()


if(__name__ == '__main__'):
    main()