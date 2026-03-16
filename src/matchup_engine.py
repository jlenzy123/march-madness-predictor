class Team:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats

    def compare(self, other_team):
        advantages = []
        disadvantages = []
        for stat in self.stats:
            if self.stats[stat] > other_team.stats.get(stat, 0):
                advantages.append((self.name, stat, self.stats[stat], other_team.name, other_team.stats.get(stat, 0)))
            elif self.stats[stat] < other_team.stats.get(stat, 0):
                disadvantages.append((self.name, stat, self.stats[stat], other_team.name, other_team.stats.get(stat, 0)))
        return advantages, disadvantages


def analyze_matchup(team1, team2):
    adv, disadv = team1.compare(team2)
    print(f"Comparing {team1.name} vs {team2.name}")
    print(f"Advantages: {adv}")
    print(f"Disadvantages: {disadv}")

# Example usage:
if __name__ == '__main__':
    team_a = Team('Team A', {'points_per_game': 75, 'rebounds_per_game': 35})
    team_b = Team('Team B', {'points_per_game': 70, 'rebounds_per_game': 30})
    analyze_matchup(team_a, team_b)
