import pandas as pd

class CoachAnalyzer:
    def __init__(self, data):
        self.data = data

    def win_percentage_by_round(self, round_name):
        total_games = self.data[self.data['round'] == round_name].shape[0]
        total_wins = self.data[(self.data['round'] == round_name) & (self.data['result'] == 'W')].shape[0]
        return total_wins / total_games if total_games > 0 else 0.0

# Example usage:
# data = pd.DataFrame(...)  # DataFrame must have 'round' and 'result' columns
# analyzer = CoachAnalyzer(data)
# print(analyzer.win_percentage_by_round('R64'))