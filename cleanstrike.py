# Clean Strike Application in python3

class CleanStrike:

    def __init__(self):
        """ There are 9 black coins, a red coin and
         a striker on the carrom-board """
        self.redcoins = 1
        self.blackcoins = 9

    def strike(self):
        """ When a player pockets a coin he/she wins a point """

    def multistrike(self):
        """ When a player pockets more than one coin he/she wins 2 points.
         All, but 2 coins, that were pocketed, get back on to the carrom-board """

    def redstrike(self):
        """ When a player pockets red coin he/she wins 3 points. 
        If other coins are pocketed along with red coin in the same turn, 
        other coins get back on to the carrom-board """

    def strikerstrike(self):
        """ When a player pockets the striker he/she loses a point """

    def defunctcoin(self):
        """ When a coin is thrown out of the carrom-board,
        due to a strike, the player loses 2 points, 
        and the coin goes out of play """

    def deductpoint(self,player):
        """ 1. When a player does not pocket a coin for 3 successive turns he/she loses a point 
            2. When a player fouls 3 times (a foul is a turn where a player loses, at least, 1 point), he/she loses an additional point """

    def showleaderboard(self):
        """ """
        
    def computewinner(self):
        """ 1. A game is won by the first player to have won at least 5 points, in total, and, at least,
                3 points more than the opponent. 
            2. When the coins are exhausted on the board, if the highest scorer is not leading by, atleast, 
                3 points or does not have a minimum of 5 points, the game is considered a draw """


""" Sample Input:
Player 1: Choose an outcome from the list below

1.Strike
2.Multistrike
3.Red strike
4.Striker strike
5.Defunct coin
6.None
1

Player 2: Choose an outcome from the list below

1.Strike
2.Multistrike
3.Red strike
4.Striker strike
5.Defunct coin
6.None
6

Player 1 won the game. Final Score: 15-11 """