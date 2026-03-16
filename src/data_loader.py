# Data Loader

import requests
import pandas as pd

class DataLoader:
    def __init__(self):
        self.team_stats_url = 'https://example.com/team_stats'
        self.bracket_data_url = 'https://example.com/bracket_data'
        self.coach_history_url = 'https://example.com/coach_history'
        self.injuries_url = 'https://example.com/injuries'

    def load_team_stats(self):
        response = requests.get(self.team_stats_url)
        return pd.DataFrame(response.json())

    def load_bracket_data(self):
        response = requests.get(self.bracket_data_url)
        return pd.DataFrame(response.json())

    def load_coach_history(self):
        response = requests.get(self.coach_history_url)
        return pd.DataFrame(response.json())

    def load_injuries(self):
        response = requests.get(self.injuries_url)
        return pd.DataFrame(response.json())

# Example usage:
# loader = DataLoader()
# team_stats = loader.load_team_stats()
# bracket_data = loader.load_bracket_data()
# coach_history = loader.load_coach_history()
# injuries = loader.load_injuries()