import pygame
import random
from pop_sprite import Pop_sprite
import math



class Ga():
    def __init__(self, size, sprite_list):
        random.seed()

        self.pop_size = size
        self.sprite_list = sprite_list
        self.population = {}
        self.target_pos = ()
        self.best_score = 1000
        self.average = 0

    def generate_pop(self, size, sprites):
        for i in range(size):
            x = random.randrange(0, 800)
            y = random.randrange(0, 800)
            new_pos = []
            new_pos.append(x)
            new_pos.append(y)
            new_ind = Pop_sprite(new_pos)
            self.population[i] = {"x": x, "y": y, "fitness": 0, "age": 0}
            sprites.add(new_ind)
        return self.population
        #print(self.population)

    def set_target(self, target_pos):
        self.target_pos = target_pos

    def find_fitness(self):
        total = 0
        for i in self.population:
            x = self.population[i]["x"]
            y = self.population[i]["y"]
            a = x - self.target_pos[0]
            b = y - self.target_pos[1]
            self.population[i]["fitness"] = math.sqrt(a**2 + b**2)
            total += self.population[i]["fitness"]
        self.average = total / self.pop_size
        print("ave: " +str(self.average))

    def select_parents(self):
        pool = {}
        pool_index = 0
        #print("population size: " + str(len(self.population)))
        while len(pool) < self.pop_size /2:
            selection = random.randrange(0, (self.pop_size))
            if self.population[selection]["fitness"] < self.average +500:# and self.population[selection]["age"] < 10:
                #print(selection)
                pool[pool_index] = self.population[selection]
                pool_index +=1
                if self.population[selection][
                    "fitness"] < self.average + 100:  # and self.population[selection]["age"] < 10:
                    # print(selection)
                    pool[pool_index] = self.population[selection]
                    pool_index += 1
                    if self.population[selection]["fitness"] < self.average:
                        pool[pool_index] = self.population[selection]
                        pool_index += 1
            #print(len(pool))


        #print("pool: ")
        #print("size :" + str(len(pool)))
        #print(pool)
        return pool
        pass

    def crossover(self, _pool):
        pool = _pool
        new_pop = {}

        _index = 0
        new_pop[0] = pool[0]
        for i in range(len(pool)):
            unique = True
            for j in range(len(new_pop)):
                if pool[i]["x"] == new_pop[j]["x"] and pool[i]["y"] == new_pop[j]["y"]:
                    unique = False

            if unique == True:
                new_pop[_index] = pool[i]
                _index += 1

        #print(len(new_pop))

        #print(len(pool))

        index = len(new_pop)
        while len(new_pop) < self.pop_size:
            p1 = random.randrange(0, len(pool))
            p2 = random.randrange(0, len(pool))
            new_pop[index] = {"x": pool[p1]["x"], "y": pool[p2]["y"], "age":0, "fitness":0}

            new_pop[index]["x"] += random.randrange(-20, 20)
            new_pop[index]["y"] += random.randrange(-20, 20)

            index +=1
        return new_pop

    def create_new_generation(self, _pool):
        pool = _pool
        return self.crossover(pool)

    def get_new_generation(self):
        if self.target_pos == ():
            return self.population

        for i in self.population:
            self.population[i]["age"] += 1

        self.find_fitness()
        pool = self.select_parents()
        #self.population.clear()
        self.population =  self.create_new_generation(pool)
        #print(self.population)
        return self.population
        pass

