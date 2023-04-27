"""
My collection of initialization methods for different representations

Student number:
Student name:
"""

#imports
import random

def permutation(pop_size, chrom_length):
    population = []
    for i in range(pop_size):
        perm = [j for j in range(chrom_length)]
        random.shuffle(perm)
        population.append(perm)
    return population
                    

