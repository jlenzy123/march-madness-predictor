def compare_matchups(team1_stats, team2_stats):
    """
    Compare two teams based on their stats and predict the matchup outcome.
    :param team1_stats: Dictionary containing stats for team 1
    :param team2_stats: Dictionary containing stats for team 2
    :return: String prediction of the matchup outcome
    """
    team1_score = team1_stats.get('offense', 0) - team2_stats.get('defense', 0)
    team2_score = team2_stats.get('offense', 0) - team1_stats.get('defense', 0)
    
    if team1_score > team2_score:
        return f'Team 1 wins!\nScore: {team1_score} to {team2_score}'
    elif team2_score > team1_score:
        return f'Team 2 wins!\nScore: {team2_score} to {team1_score}'
    else:
        return 'It’s a tie!'}