# Clean Strike Application in python3

class CleanStrike:

    def __init__(self):
        """ There are 9 black coins, a red coin and
         a striker on the carrom-board """
        self.redcoins = 1
        self.blackcoins = 9

    def strike(self):
        """ When a player pockets a coin he/she wins a point """

        if self.blackcoins == 0:
            return 0

        self.blackcoins = self.blackcoins - 1
        # print(self.blackcoins)
        return 1

    def multistrike(self):
        """ When a player pockets more than one coin he/she wins 2 points.
         All, but 2 coins, that were pocketed, get back on to the carrom-board """

        if self.blackcoins == 0:
            return 0

        self.blackcoins = 7
        self.redcoins = 1
        return 2

    def redstrike(self):
        """ When a player pockets red coin he/she wins 3 points. 
        If other coins are pocketed along with red coin in the same turn, 
        other coins get back on to the carrom-board """

        if self.redcoins == 0:
            return 0

        self.redcoins = 0
        return 3

    def striker(self):
        """ When a player pockets the striker he/she loses a point """
        return -1

    def defunctcoin(self):
        """ When a coin is thrown out of the carrom-board,
        due to a strike, the player loses 2 points, 
        and the coin goes out of play """

        if self.blackcoins == 0:
            return 0

        self.blackcoins = self.blackcoins - 1
        return -2


    def nostrike(self):
        """ No coin is put inside the pocket """
        return 0
    
    def coinchecker(self):
        if self.blackcoins == 0 or self.redcoins == 0:
            return True
        else:
            return False
    
        
    

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

class Players:

    def __init__(self):
        self.player_dict = {1 : { 'score':0, 'foulcount': 0, 'nocoinpocketed': 0 } , 2 : { 'score':0, 'foulcount': 0, 'nocoinpocketed': 0 }}

    def changescore(self,player,points):
        self.player_dict[player]['score']= self.player_dict[player]['score']+points
        
    def checkscore(self):
        if(self.player_dict[1]['score']>=5) and self.player_dict[1]['score']-self.player_dict[2]['score'] >= 3:
            return True
        elif (self.player_dict[2]['score']>=5) and self.player_dict[2]['score']-self.player_dict[1]['score'] >= 3:
            return True
        else:
            return False
            
    def deductpoint(self,player,points):
        """ 1. When a player does not pocket a coin for 3 successive turns he/she loses a point 
            2. When a player fouls 3 times (a foul is a turn where a player loses, at least, 1 point), he/she loses an additional point """

    def nocoinspocketed(self,player):
        if(self.player_dict[player]['nocoinpocketed']==2):
            self.player_dict[player]['score']-=1
            self.player_dict[player]['foulcount']+=1
            self.player_dict[player]['nocoinpocketed']=0
        else: 
            self.player_dict[player]['nocoinpocketed']+=1

    def changefoulcount(self,player):
        if(self.player_dict[player]['foulcount']==2):
            self.player_dict[player]['score']-=1
            self.player_dict[player]['foulcount']=0
        else:
            self.player_dict[player]['foulcount']+=1

        
    def showleaderboard(self):
        """ """
        print("Leaderboard")
        print(self.player_dict)
        """
        The following checks the score of a player and returns the result.
        :return: object containing result, player1score, player2score
        """
        if self.player_dict[1]['score'] > self.player_dict[2]['score']:
            if self.player_dict[1]['score'] - self.player_dict[2]['score'] >= 3:
                return {"result": "Player1",
                        "Player1 Score": self.player_dict[1]['score'],
                        "Player2 Score": self.player_dict[2]['score']}

        else:
            if self.player_dict[2]['score'] - self.player_dict[1]['score'] >= 3:
                return {"result": "Player2",
                        "Player1 Score": self.player_dict[1]['score'],
                        "Player2 Score": self.player_dict[2]['score']}
            

        return {"result": "Draw",
                "Player1 Score": self.player_dict[1]['score'],
                "Player2 Score": self.player_dict[2]['score']}

    def computewinner(self):
        """ 1. A game is won by the first player to have won at least 5 points, in total, and, at least,
                3 points more than the opponent. 
            2. When the coins are exhausted on the board, if the highest scorer is not leading by, atleast, 
                3 points or does not have a minimum of 5 points, the game is considered a draw """



print("Welcome to Clean Strike Carrom Game!")

gameplayers = Players()
game=CleanStrike()
player=0

while(True):

    
    player = (player) % 2
    player = player+1

    print("Player ",player)
    print("Choose an outcome from the list below:")
    print("1.Strike\n 2.Multistrike\n 3.Red strike\n 4.Striker strike\n 5.Defunct coin\n 6.None")
    choice = int(input())

    if choice == 1:
        points = game.strike()
        gameplayers.changescore(player,points)

    elif choice == 2:
        points = game.multistrike()
        gameplayers.changescore(player,points)
    
    elif choice == 3:
        points = game.redstrike()
        gameplayers.changescore(player,points)

    elif choice == 4:
        points = game.striker()
        gameplayers.changescore(player,points)
        gameplayers.changefoulcount(player)
        gameplayers.nocoinspocketed(player)
        #foulcount ++
        #nocoinspocket ++

    elif choice == 5:
        points = game.defunctcoin()
        gameplayers.changescore(player,points)
        gameplayers.changefoulcount(player)
        gameplayers.nocoinspocketed(player)
        #foulcount - 1
        #nocoinspocket ++

    elif choice == 6:
        gameplayers.nocoinspocketed(player)
        #nocoinspocket ++

    gameplayers.showleaderboard()
    if game.coinchecker() or gameplayers.checkscore():
        print(gameplayers.showleaderboard())
        break







# gameplayers.callswitchstatement(choice,player=1)

# print("Player2\n")
# print("Choose an outcome from the list below:\n")
# print("1.Strike\n2.Multistrike\n3.Red strike\n4.Striker strike\n5.Defunct coin\n6.None\n")
# choice = int(input())
# gameplayers.callswitchstatement(choice,player=2)
