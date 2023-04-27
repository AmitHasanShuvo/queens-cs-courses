"""
My collection of fitness evaluation methods

Student number:
Student name:
"""

#imports


def fitness_8queen(individual):
    fitness = 0
    n = len(individual)
    for i in range(n):
        for j in range(i+1, n):
            if abs(i-j) == abs(individual[i]-individual[j]):
                fitness -= 1
            else:
                fitness += 1
    return fitness


