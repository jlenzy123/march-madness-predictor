# Example code to predict Round 1 matchups

def predict_round_1(matchups):
    predictions = {}
    for matchup in matchups:
        # Simple example logic for prediction
        predictions[matchup] = matchup[0]  # Predict the first team to win
    return predictions

# Example matchups
round_1_matchups = [('Team A', 'Team B'), ('Team C', 'Team D')]

# Making predictions
predictions = predict_round_1(round_1_matchups)
print(predictions)