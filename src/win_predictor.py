import pandas as pd
import numpy as np

class WinPredictor:
    def __init__(self, team_stats):
        self.team_stats = team_stats

    def calculate_win_probability(self, team_a, team_b):
        # Example calculation based on statistical differences
        stats_a = self.team_stats[team_a]
        stats_b = self.team_stats[team_b]

        # Calculate win probability
        stat_diff = np.array(stats_a) - np.array(stats_b)
        probability = 1 / (1 + np.exp(-np.sum(stat_diff)))

        return probability

# Example team statistics
team_stats = {
    'Team A': [120, 90, 30, 40, 50],  # Example statistics for Team A
    'Team B': [110, 85, 35, 42, 48]   # Example statistics for Team B
}

predictor = WinPredictor(team_stats)
win_probability = predictor.calculate_win_probability('Team A', 'Team B')
print(f'Win Probability of Team A over Team B: {win_probability:.2f}')