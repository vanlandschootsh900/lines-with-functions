#Shay VanLandschoot
#--DATE--#
# Pygame game template

import pygame
import sys
import config # Import the config module

def init_game ():

    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) 
# Use constants from config
    
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events ():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True


def draw_line(screen, line_color, start_point, end_point, width):
    pygame.draw.line(screen, line_color, start_point, end_point, width)



def main():
    screen = init_game()
    clock = pygame.time.Clock()
    

    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE) # Use color from config
        

        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS)

        
        #arg 1
        start_pos1=[800,600]
        end_pos1=[0,0]
        line_color1= config.RED
        line_thickness1= 12
        
        #arg2
        start_pos2=[0,600]
        end_pos2= [800,0]
        line_color2= config.RED
        line_thickness2= 12

        draw_line(screen, line_color1, start_pos1, end_pos1, line_thickness1)
        draw_line(screen, line_color2, start_pos2, end_pos2, line_thickness2)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()