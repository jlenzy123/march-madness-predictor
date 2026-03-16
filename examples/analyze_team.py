# Analyze Team Statistics

import pandas as pd
import matplotlib.pyplot as plt

class TeamAnalyzer:
    def __init__(self, team_name, data_file):
        self.team_name = team_name
        self.data = pd.read_csv(data_file)

    def get_team_stats(self):
        # Filter data for the specific team
        team_data = self.data[self.data['team'] == self.team_name]
        return team_data

    def plot_team_performance(self):
        team_data = self.get_team_stats()
        plt.figure(figsize=(10, 6))
        plt.plot(team_data['year'], team_data['wins'], label='Wins')
        plt.plot(team_data['year'], team_data['losses'], label='Losses')
        plt.title(f'{self.team_name} Performance Over the Years')
        plt.xlabel('Year')
        plt.ylabel('Games')
        plt.legend()
        plt.grid()
        plt.show()

    def analyze_tournament_prospects(self):
        team_data = self.get_team_stats()
        avg_wins = team_data['wins'].mean()
        avg_losses = team_data['losses'].mean()
        print(f'Average Wins: {avg_wins}, Average Losses: {avg_losses}')

# Example usage:
# analyzer = TeamAnalyzer('Duke', 'tournament_data.csv')
# analyzer.plot_team_performance()
# analyzer.analyze_tournament_prospects()