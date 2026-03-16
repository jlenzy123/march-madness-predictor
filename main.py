import random

# Teams and seedings
teams = {
    'Duke': 1,
    'Florida': 1,
    'Michigan': 1,
    'Arizona': 1,
    'North Carolina': 2,
    'Alabama': 2,
    'Purdue': 2,
    'Gonzaga': 2,
    'Ohio State': 3,
    'Texas': 3,
    'Houston': 3,
    'USC': 3
}

# Simulation parameters
iterations = 10000
results = {team: 0 for team in teams}

# Simulate the tournament
for _ in range(iterations):
    winner = random.choices(list(teams.keys()), weights=[4-seed for seed in teams.values()], k=1)[0]
    results[winner] += 1

# Display results
for team, wins in results.items():
    print(f'{team}: {wins / iterations:.2%}')