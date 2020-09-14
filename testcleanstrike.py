import unittest
from cleanstrike import playgame


class TestPlayGame(unittest.TestCase):
    def test_given_sample(self):
        """
        Test that it can produce the same output as given 
        """
        player_input =[2,1,1,2,1,2,2,4,6,1,1,6,4,1,2,1,6,2,2,6,1,1,1,1,3]
        result = playgame(player_input)
        self.assertEqual(result, 1)

    def test_blackcoins_exhausted(self):
        """
        Test that it can display results when blackcoins are exhausted
        """
        player_input =[1,2,1,1,1,1,1,1,6,1]
        result = playgame(player_input)
        self.assertEqual(result, 0)

    def test_redcoins_exhausted(self):
        """
        Test that it can display results when redcoins are exhausted
        """
        player_input =[1,2,2,3]
        result = playgame(player_input)
        self.assertEqual(result, 0)

    def test_declare_result_when_highest_player_greater_than_5_and_difference_greater_than_3(self):
        """
        Test that it can check the given condition: 
            A game is won by the first player to have won at least 5 points, in total, 
            and, at least, 3 points more than the opponent
        """
        player_input =[2,2,1,2,5,1]
        result = playgame(player_input)
        self.assertEqual(result, 2)

    def test_draw_condition(self):
        """
        Test that it can check the given condition:
            When the coins are exhausted on the board, if the highest scorer is not leading by, 
            atleast, 3 points or does not have a minimum of 5 points, the game is considered a draw
        """
        player_input =[2,2,1,6,5,1,1,1,1,1]
        result = playgame(player_input)
        self.assertEqual(result, 0)

    def test_unexpected_input(self):
        """
        Test that it can ignore the input if it is unexpected 
        """
        player_input =[1,2,2,2,1,2,1,7,2]
        result = playgame(player_input)
        self.assertEqual(result, 2)

    def test_nocoins_pocketed_successively_thrice(self):
        """
        Test that it can decrease the score by 1 when the player does not pocket a coin for 3 successive turns:
        """
        player_input =[2,1,1,2,6,1,4,6,6,1]
        result = playgame(player_input)
        self.assertEqual(result, 2)


    def test_when_foulcount_reaches_three(self):
        """
        Test that it can decrease the score by 1 when a player fouls 3 times
        """
        player_input =[2,1,2,1,4,1,5,1,1,6,4,1]
        result = playgame(player_input)
        self.assertEqual(result, 2)

    def test_negative_score(self):
        """
        Test that the score never goes below 0
        """
        player_input =[2,1,2,1,5,1,5,1,1,6,4,1]
        result = playgame(player_input)
        self.assertEqual(result, 2)


    
if __name__ == '__main__':
    unittest.main()