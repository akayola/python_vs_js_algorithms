'''
   Evolutionary Algorithm
   Genetic Algorith works in two steps:
   1. Create Initial Population
   2. Evolution
   Genetic Algorithm is not guaranteed to find the absolute best solution.
   It attempts to find the global best while avoiding local best solutions.
   Find value of x, y, z numbers to satisfy calculation
'''

import random

def calculate_result(x, y, z):
    return 8 * x ** 3 + 9 * y ** 4 + 89 * z ** 2 - 73

def get_rank(x, y, z):
    answer = calculate_result(x, y, z)
    if answer == 0:
        return 9999
    else:
        return abs(1 / answer)

# Create Initial Population - creating a random population of potential solutions.
# Generate list of random solutions [(x, y, z), (x, y, z), ...]
# random.uniform() method returns a random floating number between the two specified numbers (both included).
solutions = []
for _ in range(10000):
    solutions.append((random.uniform(0, 10000),
                      random.uniform(0, 10000),
                      random.uniform(0, 10000)))

# Evolution - evolve Initial Population through the number of generations.
# Evolution has 3 steps:
# Step 1 Survivors - pass initial population through filter, choose remaining survivors.
# Step 2 Crossover - combine remaining survivors to produce new solutions.
# Step 3 Mutation - apply mutations to our solutions.

for i in range(10000):
    ranked_solutions = []

    for s in solutions:
        # Step 1 - Survivors
        # Get rank of each solution, append to ranked_solutions list as following:
        # (rank, (x, y, z))
        # (5122.111650284931, (0.8080054678645973, 0.8023505238263668, 0.8041916276363511))
        ranked_solutions.append((get_rank(s[0], s[1], s[2]), s))

    ranked_solutions.sort()
    ranked_solutions.reverse()

    print(f'=== generate {i} best solutions ===')
    print(ranked_solutions[0])

    if ranked_solutions[0][0] > 999:
        break

    best_solutions = ranked_solutions[:100]

    #
    survivors = []
    midway = len(ranked_solutions) // 2
    for i in range(midway):
        if ranked_solutions[i][0] > ranked_solutions[i + midway][0]:
            survivors.append([ranked_solutions[i][1][0],
                              ranked_solutions[i][1][1],
                              ranked_solutions[i][1][2]])
        else:
            survivors.append([ranked_solutions[i + midway][1][0],
                              ranked_solutions[i + midway][1][1],
                              ranked_solutions[i + midway][1][2]])

    # Step2 - Crossover
    offspring = []
    midway = len(survivors) // 2
    for i in range(midway):
        parent_a, parent_b = survivors[i], survivors[i + midway]
        offspring.append(parent_a)
        offspring.append(parent_a)

    # Step 3 - Mutations
    new_generation = []
    for _ in range(100):
        element1 = random.choice(offspring[0]) * random.uniform(0.99, 1.01)
        element2 = random.choice(offspring[1]) * random.uniform(0.99, 1.01)
        element3 = random.choice(offspring[2]) * random.uniform(0.99, 1.01)

        new_generation.append((element1, element2, element3))
    solutions = new_generation

