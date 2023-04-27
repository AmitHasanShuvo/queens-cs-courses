"""
My collection of recombination methods

Student number:
Student name:
"""

#imports
import random

def permutation_cut_and_crossfill(parent1, parent2):
    n = len(parent1)
    cut1 = random.randint(0, n-1)
    cut2 = random.randint(cut1+1, n)
    offspring1 = parent1[:cut1] + parent2[cut1:cut2]
    offspring2 = parent2[:cut1] + parent1[cut1:cut2]
    for i in parent2:
        if i not in offspring1:
            offspring1.append(i)
    for i in parent1:
        if i not in offspring2:
            offspring2.append(i)
    return offspring1, offspring2