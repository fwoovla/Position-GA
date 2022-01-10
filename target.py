import pygame

class Target(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Target, self).__init__()
        self.pos = pos
        self.image = pygame.Surface([20,20])
        self.image.fill((255,255,255))
        self.image.set_colorkey((255,255,255))
        pygame.draw.circle(self.image, (200, 40, 47), [10,10], 5)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x = self.pos[0] -10
        self.rect.y = self.pos[1] -10
