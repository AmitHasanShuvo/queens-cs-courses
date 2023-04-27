"""
My collection of survivor selection methods

Student number:
Student name:
"""

#imports

import numpy as np

def mu_plus_lambda(current_pop, current_fitness, offspring, offspring_fitness):
    """mu+lambda selection"""
    population = []
    fitness = []

    # Combine current population and offspring
    current_pop = np.array(current_pop)
    offspring = np.array(offspring)
    combined_pop = np.concatenate((current_pop, offspring.reshape(-1, current_pop.shape[1])))

    ##combined_pop = np.concatenate((current_pop, np.array(offspring).reshape(-1, current_pop.shape[1])))
    combined_fitness = np.concatenate((current_fitness, offspring_fitness))
    
    # Sort the combined population by their fitness values
    sorted_idx = np.argsort(combined_fitness)
    sorted_pop = combined_pop[sorted_idx]
    sorted_fitness = combined_fitness[sorted_idx]
    
    # Select the best mu individuals from the combined population
    mu = len(current_pop)
    population = sorted_pop[:mu]
    fitness = sorted_fitness[:mu]
    
    return population, fitness


def replacement(current_pop, current_fitness, offspring, offspring_fitness):
    """replacement selection"""

    population = []
    fitness = []

    # Combine current population and offspring
    combined_pop = np.concatenate((current_pop, offspring))
    combined_fitness = np.concatenate((current_fitness, offspring_fitness))
    
    # Sort the combined population by their fitness values
    sorted_idx = np.argsort(combined_fitness)
    sorted_pop = combined_pop[sorted_idx]
    sorted_fitness = combined_fitness[sorted_idx]
    
    # Replace the current population with the best mu individuals from the combined population
    mu = len(current_pop)
    population = sorted_pop[:mu]
    fitness = sorted_fitness[:mu]
    
    return population, fitness


def random_uniform(current_pop, current_fitness, offspring, offspring_fitness):
    """random uniform selection"""
    population = []
    fitness = []

    # Combine current population and offspring
    combined_pop = np.concatenate((current_pop, offspring))
    combined_fitness = np.concatenate((current_fitness, offspring_fitness))
    
    # Randomly select mu individuals from the combined population with uniform probability
    mu = len(current_pop)
    idx = np.random.choice(len(combined_pop), mu, replace=False)
    population = combined_pop[idx]
    fitness = combined_fitness[idx]
    
    return population, fitness


