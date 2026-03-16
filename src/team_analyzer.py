class Team:
    def __init__(self, name, wins, losses, points_for, points_against):
        self.name = name
        self.wins = wins
        self.losses = losses
        self.points_for = points_for
        self.points_against = points_against

    def win_percentage(self):
        total_games = self.wins + self.losses
        return self.wins / total_games if total_games > 0 else 0

    def points_difference(self):
        return self.points_for - self.points_against
    
    def composite_metric(self):
        return self.win_percentage() + (self.points_difference() / 100)