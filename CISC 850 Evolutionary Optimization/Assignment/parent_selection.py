"""
My collection of parent selection methods

Student number:
Student name:
"""

# imports

import random


def MPS(fitness, mating_pool_size):
    total_fitness = sum(fitness)
    probability = [f/total_fitness for f in fitness]
    parents_index = []
    for i in range(mating_pool_size):
        r = random.random()
        s = 0
        for j in range(len(fitness)):
            s += probability[j]
            if s >= r:
                parents_index.append(j)
                break
    return parents_index

def tournament(fitness, mating_pool_size, tournament_size):
    parents_index = []
    for i in range(mating_pool_size):
        competitors = random.sample(range(len(fitness)), tournament_size)
        best = max(competitors, key=lambda x: fitness[x])
        parents_index.append(best)
    return parents_index

def random_uniform(pop_size, mating_pool_size):
    parents_index = random.sample(range(pop_size), mating_pool_size)
    return parents_index
