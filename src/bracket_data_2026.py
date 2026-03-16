# 2026 March Madness Tournament Bracket Data

# Data structure for storing team data
tournament_bracket = {
    "East": {
        "1": {"team": "Team A", "stats": {"wins": 30, "losses": 2}},
        "2": {"team": "Team B", "stats": {"wins": 28, "losses": 4}},
        # Add more teams as needed
    },
    "West": {
        "1": {"team": "Team C", "stats": {"wins": 29, "losses": 3}},
        "2": {"team": "Team D", "stats": {"wins": 27, "losses": 5}},
        # Add more teams as needed
    },
    # Continue for South and Midwest regions
    "South": {},
    "Midwest": {}
}

def print_bracket(bracket):
    for region, teams in bracket.items():
        print(f"Region: {region}")
        for seed, data in teams.items():
            print(f"Seed {seed}: {data['team']} (Wins: {data['stats']['wins']}, Losses: {data['stats']['losses']})")

# Print the tournament bracket
print_bracket(tournament_bracket)