
import pygame

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # fechou, executo mesmo
            pygame.quit()
            quit()  # acabar com o pygame (init)
