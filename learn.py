
from time import sleep #from time  impotts the sleep library
import pygame #imports pygame library

pygame.init()#intaling py game

def main():
    
    # Set up the drawing window
    screen = pygame.display.set_mode([500, 500])
    
    pygame.display.set_caption("cool shop")
    
    # Fill the background with white
    screen.fill((255, 255, 255))
    
    
    #drawing
    pygame.draw.rect(screen, "black", [150, 150, 200 , 200]) #Draw a black rectangle in the chanter
    pygame.draw.circle(screen, "red", [255 , 255] , 3) # Draw a red blue circle in the center
    pygame.draw.polygon(screen,"blue", ((0, 0), (0, 50), (25, 75), (50, 50), (50, 0))) # Draw a blue polygon in corner
   
    #add text
    font = pygame.font.SysFont(None, 20)
    img = font.render('sound', True, "white")
    screen.blit(img, (5, 5))
    
    
    soundObj = pygame.mixer.Sound('punch.wav')

    # Run until the user asks to quit
    running = True
    
    #vhange now to gray
    change = True 
    while running:
        
        for event in pygame.event.get(): #alll events
            if event.type == pygame.QUIT: #quit
                running = False
            
            
        
        pygame.display.flip()
       

    # Done! Time to quit.
    pygame.quit()


if(__name__ == '__main__'):
    main()