import pygame

class Pop_sprite(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Pop_sprite, self).__init__()
        self.pos = pos
        self.image = pygame.Surface([20,20])
        self.image.fill((255,255,255))
        self.image.set_colorkey((255,255,255))
        pygame.draw.circle(self.image, (47, 186, 0), [10,10], 5)
        self.rect = self.image.get_rect()
        self.color = (47, 186, 0)

    def update(self):
        pygame.draw.circle(self.image, self.color, [10, 10], 5)
        self.rect.x = self.pos[0] -10
        self.rect.y = self.pos[1] -10