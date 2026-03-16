import random

class Team:
    def __init__(self, name, wins, losses, ppg, papg, rebounds):
        self.name = name
        self.wins = wins
        self.losses = losses
        self.ppg = ppg  # Points per Game
        self.papg = papg  # Points Allowed Per Game
        self.rebounds = rebounds

    def __str__(self):
        return f'{self.name} | Wins: {self.wins}, Losses: {self.losses}, PPG: {self.ppg}, PAPG: {self.papg}, Rebounds: {self.rebounds}'

# Sample Data:  Let's assume these variables hold real statistics for the teams
teams = {
    'East': [
        Team('Team A', 25, 5, 80, 70, 38),
        Team('Team B', 22, 8, 75, 72, 35),
        # Add real team data
    ],
    'South': [
        Team('Team C', 30, 2, 85, 65, 40),
        Team('Team D', 21, 9, 78, 74, 32),
        # Add real team data
    ],
    'Midwest': [
        Team('Team E', 20, 10, 72, 76, 36),
        Team('Team F', 24, 6, 79, 68, 34),
        # Add real team data
    ],
    'West': [
        Team('Team G', 26, 4, 82, 69, 39),
        Team('Team H', 19, 11, 71, 77, 33),
        # Add real team data
    ]
}

# Simulate a match between two teams
def simulate_match(team1, team2):
    score1 = (team1.ppg + team1.rebounds * 0.5) - (team2.papg * 0.3) + random.uniform(-5, 5)
    score2 = (team2.ppg + team2.rebounds * 0.5) - (team1.papg * 0.3) + random.uniform(-5, 5)
    return team1, team2, score1, score2

# Run the tournament simulation
def simulate_tournament():
    winners = []
    for region, teams in teams.items():
        while len(teams) > 1:
            team1 = teams.pop(0)
            team2 = teams.pop(0)
            team1, team2, score1, score2 = simulate_match(team1, team2)
            winners.append(team1 if score1 > score2 else team2)
            print(f'Simulating: {team1.name} vs {team2.name} - {score1:.1f} vs {score2:.1f}')
        print(f'Winner of {region}: {winners[-1].name}')

if __name__ == '__main__':
    simulate_tournament()