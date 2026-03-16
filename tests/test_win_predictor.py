import unittest
from win_predictor import predict_winner

class TestWinPredictor(unittest.TestCase):

    def test_predict_winner(self):
        # Example test case
        self.assertEqual(predict_winner(team_a, team_b), expected_winner)

if __name__ == '__main__':
    unittest.main()