"""
My colleciton of mutation methods

Student number:
Student name:
"""

# imports


import random

def permutation_swap(individual):
    n = len(individual)
    i, j = random.sample(range(n), 2)
    individual[i], individual[j] = individual[j], individual[i]
    return individual

