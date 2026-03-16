def analyze_coach_tournament_history(coach_name, tournament_data):
    """
    Analyze the tournament history of a coach by rounds.
    
    Args:
        coach_name (str): Name of the coach.
        tournament_data (list of dict): List containing tournament data for each game with keys 'round', 'coach', 'result'.
    
    Returns:
        dict: A dictionary containing the win-loss record by round.
    """
    round_record = {}
    for game in tournament_data:
        if game['coach'] == coach_name:
            round_name = game['round']
            if round_name not in round_record:
                round_record[round_name] = {'wins': 0, 'losses': 0}
            if game['result'] == 'win':
                round_record[round_name]['wins'] += 1
            else:
                round_record[round_name]['losses'] += 1
    return round_record

# Example usage:
# tournament_data = [
#     {'round': 'First Round', 'coach': 'Coach A', 'result': 'win'},
#     {'round': 'Second Round', 'coach': 'Coach A', 'result': 'loss'},
#     {'round': 'Final Four', 'coach': 'Coach A', 'result': 'win'}
# ]
# print(analyze_coach_tournament_history('Coach A', tournament_data))