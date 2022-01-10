import pygame

def update_click(screen, target):
    image = pygame.Surface([20,20])
    image.fill()
    pygame.Surface.blit(screen, image, target)