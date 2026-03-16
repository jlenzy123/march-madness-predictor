import random
import numpy as np
import matplotlib.pyplot as plt

class Tournament:
    def __init__(self, teams):
        self.teams = teams
        self.n = len(teams)

    def simulate_match(self, team1, team2):
        return team1 if random.random() < 0.5 else team2

    def simulate_tournament(self):
        matches = self.teams
        while len(matches) > 1:
            matches = [self.simulate_match(matches[i], matches[i + 1]) for i in range(0, len(matches), 2)]
        return matches[0]

    def run_simulations(self, n_simulations=10000):
        results = []
        for _ in range(n_simulations):
            winner = self.simulate_tournament()
            results.append(winner)
        return results

    def generate_probability_distribution(self, results):
        unique_winners = list(set(results))
        probabilities = {winner: results.count(winner) / len(results) for winner in unique_winners}
        return probabilities

if __name__ == '__main__':
    teams = ['Team A', 'Team B', 'Team C', 'Team D']  # Example team names
    tournament = Tournament(teams)
    results = tournament.run_simulations(10000)
    probabilities = tournament.generate_probability_distribution(results)

    # Plotting the probability distribution
    plt.bar(probabilities.keys(), probabilities.values())
    plt.xlabel('Teams')
    plt.ylabel('Probability of Winning')
    plt.title('Tournament Probability Distribution')
    plt.show()