import random

class Team:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

class Game:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

        # The probability of team1 winning is calculated based on their relative strength
        self.probability_team1_wins = self.calculate_probability()

    def calculate_probability(self):
        return self.team1.strength / (self.team1.strength + self.team2.strength)

    def play(self):
        return self.team1 if random.random() < self.probability_team1_wins else self.team2

class Tournament:
    def __init__(self, teams):
        self.teams = teams

    def run(self):
        while len(self.teams) > 1:
            next_round = []
            for i in range(0, len(self.teams), 2):
                game = Game(self.teams[i], self.teams[i + 1])
                winner = game.play()
                next_round.append(winner)
            self.teams = next_round
        return self.teams[0]

def simulate_tournament(teams, simulations):
    results = {team.name: 0 for team in teams}
    for _ in range(simulations):
        winner = Tournament(teams).run()
        results[winner.name] += 1
    return results

if __name__ == '__main__':
    teams = [Team('Team A', 1), Team('Team B', 0.75), Team('Team C', 0.5), Team('Team D', 0.25)]
    simulations = 10000
    results = simulate_tournament(teams, simulations)
    print('Simulation Results:', results)