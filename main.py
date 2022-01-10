import pygame
from target import Target
from pop_sprite import Pop_sprite
from ga import Ga
import random

# ______COLORS___________
white = (255,255,255)
red = (128, 13, 13)
blue = (22, 29, 97)
green = (47, 186, 47)
black = (0,0,0)
cyan = (29, 128, 119)
yellow = (133, 129, 30)
brown = (56, 37, 11)
#______END_COLORS________

#_______VARS_______
target = Target([0,0])
target_image = pygame.Surface([20,20])
sprites = pygame.sprite.Group()
sprites.add(target)

population = []
pop_size = 1000

ga = Ga(pop_size, sprites)
#_______END_VARS_____

screen = pygame.display.set_mode([800,800])
pygame.display.set_caption("Position GA")

running = True
clock = pygame.time.Clock()
FPS = 60

if __name__ == '__main__':
    random.seed()

    population = ga.generate_pop(pop_size, sprites)
    print("starting population")
    #print(population)
    while running:
        screen.fill(blue)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                target_pos = pygame.mouse.get_pos()
                target.pos = target_pos
                ga.set_target(target_pos)
        population = ga.get_new_generation()
        #print(ga.average)

        avg = 0
        for i in population:
            sp = Pop_sprite([int(population[i]["x"]), population[i]["y"]])
            sprites.add(sp)
            if population[i]["age"] > 0:
                sp.color = (168, 123, 50)
            if population[i]["age"] > 1:
                sp.color = (168, 80, 50)

        sprites.add(target)
        sprites.update()
        sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
        sprites.empty()
