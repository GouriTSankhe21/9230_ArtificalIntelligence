import random
import math

# Define the cities and their locations
cities = {
    'A': (0, 0),
    'B': (0, 1),
    'C': (1, 0),
    'D': (1, 1)
}

# Define the population size and number of generations
POPULATION_SIZE = 20
NUM_GENERATIONS = 50

# Define the mutation rate (i.e. the probability that a gene will be mutated)
MUTATION_RATE = 0.1

# Define the fitness function
def fitness(solution):
    total_distance = 0
    for i in range(len(solution)-1):
        city1 = solution[i]
        city2 = solution[i+1]
        distance = math.sqrt((cities[city1][0]-cities[city2][0])**2 + (cities[city1][1]-cities[city2][1])**2)
        total_distance += distance
    return 1/total_distance

# Define the crossover function (i.e. how to combine two parent solutions)
def crossover(parent1, parent2):
    child = ['']*len(parent1)
    start = random.randint(0, len(parent1)-1)
    end = random.randint(0, len(parent1)-1)
    if start > end:
        start, end = end, start
    for i in range(start, end+1):
        child[i] = parent1[i]
    j = 0
    for i in range(len(parent2)):
        if j == start:
            j = end + 1
        if parent2[i] not in child:
            child[j] = parent2[i]
            j += 1
    return child

# Define the mutation function (i.e. how to randomly change a gene in a solution)
def mutate(solution):
    for i in range(len(solution)):
        if random.random() < MUTATION_RATE:
            j = random.randint(0, len(solution)-1)
            solution[i], solution[j] = solution[j], solution[i]
    return solution

# Generate an initial population of solutions
population = []
for i in range(POPULATION_SIZE):
    solution = list(cities.keys())
    random.shuffle(solution)
    population.append(solution)

# Iterate through the generations
for gen in range(NUM_GENERATIONS):
    # Evaluate the fitness of each solution in the population
    fitness_scores = [fitness(solution) for solution in population]

    # Select the parents for the next generation using roulette wheel selection
    total_fitness = sum(fitness_scores)
    probabilities = [fitness_score/total_fitness for fitness_score in fitness_scores]
    parents = random.choices(population, weights=probabilities, k=2)

    # Generate the next generation using crossover and mutation
    offspring = []
    for i in range(POPULATION_SIZE):
        child = crossover(parents[0], parents[1])
        child = mutate(child)
        offspring.append(child)

    # Replace the current population with the offspring
    population = offspring

# Find the best solution in the final population
best_solution = max(population, key=fitness)
print('Best solution:', best_solution)
print('Distance:', 1/fitness(best_solution))
