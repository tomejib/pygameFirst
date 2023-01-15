# imports pygame library
from time import sleep
from rectGame import Rect
import pygame
pygame.init()  # intaling py game


def main():

    # Set up the drawing window
    screen = pygame.display.set_mode([500, 500])

    pygame.display.set_caption("cool shop")

    # Fill the background with white
    screen.fill((255, 255, 255))

    a = Rect("white",5,5,screen, 55, 55, 0)
    
    # drawing
    # Draw a black rectangle in the chanter
    pygame.draw.rect(screen, "black", [150, 150, 200, 200])
    # Draw a red blue circle in the center
    pygame.draw.circle(screen, "red", [255, 255], 3)
    # Draw a blue polygon in corner
    pygame.draw.polygon(screen, "blue", ((0, 0), (0, 50),
                        (25, 75), (50, 50), (50, 0)))

    # add text
    font = pygame.font.SysFont(None, 20)
    text_put = font.render('sound', True, "white")
    screen.blit(text_put, (5, 5))

    soundObj = pygame.mixer.Sound('punch.wav')

    # Run until the user asks to quit
    running = True

    # vhange now to gray
    change = True
    while running:
        for event in pygame.event.get():  # alll events
            
            if event.type == pygame.QUIT:  # quit
                running = False

            
            # event clicked
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                
                if 150 < pos[0] < 350 and 150 < pos[1] < 350:
                    
                    
                
                    if (change):  # draw gray rectangle
                        pygame.draw.rect(screen, "gray", [150, 150, 200, 200])
                        change = False

                    else:  # draw black rectangle
                        pygame.draw.rect(screen, "black", [150, 150, 200, 200])
                        change = True

                # sounds
                if 0 < pos[0] < 50 and 0 < pos[1] < 75:
                    # Draw a blue polygon in corner
                    pygame.draw.polygon(
                        screen, "green", ((0, 0), (0, 50), (25, 75), (50, 50), (50, 0)))
                    pygame.display.flip()
                    soundObj.play()#playing sound
                    sleep(0.5)
                    # Draw a blue polygon in corner
                    pygame.draw.polygon(
                        screen, "blue", ((0, 0), (0, 50), (25, 75), (50, 50), (50, 0)))
                    screen.blit(text_put, (5, 5))  # drawing text

                # Draw a red blue circle in the center
                pygame.draw.circle(screen, "red", [255, 255], 3)
                a.draw()
                print(pos)

        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()


if (__name__ == '__main__'):
    main()
