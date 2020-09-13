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
        """ When a coin is thrown out of the carrom-board, due to a strike, 
        the player loses 2 points, and the coin goes out of play """

        if self.blackcoins == 0:
            return 0

        self.blackcoins = self.blackcoins - 1
        return -2


    def nostrike(self):
        """ No coin is put inside the pocket """
        return 0
    
    def coinchecker(self):
        """ This utility function checks if black or red coins are exhausted """

        if self.blackcoins == 0 or self.redcoins == 0:
            return True
        else:
            return False
    


class Players:

    def __init__(self):
        self.player_dict = {1 : { 'score':0, 'foulcount': 0, 'nocoinpocketed': 0 } , 2 : { 'score':0, 'foulcount': 0, 'nocoinpocketed': 0 }}

    def changescore(self,player,points):
        """ This utility function is used to change the score of the player according to the points """

        self.player_dict[player]['score']= self.player_dict[player]['score']+points
        
    def checkscore(self):
        """ This utility function is used to check the given condition:
                A game is won by the first player to have won at least 5 points, in total, 
                and, at least, 3 points more than the opponent """

        if(self.player_dict[1]['score']>=5) and self.player_dict[1]['score']-self.player_dict[2]['score'] >= 3:
            return 1
        elif (self.player_dict[2]['score']>=5) and self.player_dict[2]['score']-self.player_dict[1]['score'] >= 3:
            return 2
        else:
            return 0

    def nocoinspocketed(self,player):
        """ This utility fuction is used to do the following when a player doesn't pocket a coin in his turn:
            1. Update the nocoinspocketed field in the dictionary.
            2. Update the foulcount field when the player does not pocket a coin for 3 successive turns
            3. Decrease the score by 1 when the player does not pocket a coin for 3 successive turns """

        if(self.player_dict[player]['nocoinpocketed']==2):
            self.player_dict[player]['score']-=1
            self.player_dict[player]['foulcount']+=1
            self.player_dict[player]['nocoinpocketed']=0
        else: 
            self.player_dict[player]['nocoinpocketed']+=1

    def changefoulcount(self,player):
        """ This utility function is used to uodate the foulcount when the player loses a point:
            1. Update the foulcount field
            2. When a player fouls 3 times, decrease the score by 1 """

        if(self.player_dict[player]['foulcount']==2):
            self.player_dict[player]['score']-=1
            self.player_dict[player]['foulcount']=0
        else:
            self.player_dict[player]['foulcount']+=1


    # def show_results_on_coins_exhausted(self):
    #     if self.player_dict[1]['score'] > self.player_dict[2]['score'] or self.player_dict[1]['score'] - self.player_dict[2]['score'] >= 3:
    #             # return {"result": "Player1 won",
    #             #         "Player1 Score": self.player_dict[1]['score'],
    #             #         "Player2 Score": self.player_dict[2]['score']}
    #             return 1

    #     elif self.player_dict[2]['score'] > self.player_dict[1]['score'] or self.player_dict[2]['score'] - self.player_dict[1]['score'] >= 3:
    #             # return {"result": "Player2 won",
    #             #         "Player1 Score": self.player_dict[1]['score'],
    #             #         "Player2 Score": self.player_dict[2]['score']}
    #             return 2
            

    #     # return {"result": "Draw",
    #     #         "Player1 Score": self.player_dict[1]['score'],
    #     #         "Player2 Score": self.player_dict[2]['score']}

    #     return 0


    def showWinner(self):
        """
        This utility fuction is used to check the score of players and return the winner
        """
        if self.player_dict[1]['score'] > self.player_dict[2]['score']:
            # return {"result": "Player1 won",
            #     "Player1 Score": self.player_dict[1]['score'],
            #     "Player2 Score": self.player_dict[2]['score']}
            return 1
        else:
            # return {"result": "Player2 won",
            #     "Player1 Score": self.player_dict[1]['score'],
            #     "Player2 Score": self.player_dict[2]['score']}
            return 2
        

    def showleaderboard(self):
        """ This utility function is used to show the score table after every turn """

        print("Leaderboard")
        print(self.player_dict)


def playgame(player_input):
    
    gameplayers = Players()
    game=CleanStrike()
    player=0
    print("Welcome to Clean Strike Carrom Game!")

    for i in player_input:
        player = (player) % 2
        player = player+1

        print("Player ",player)
        print("Choose an outcome from the list below:")
        print("1.Strike")
        print("2.Multistrike")
        print("3.Red strike")
        print("4.Striker strike")
        print("5.Defunct coin")
        print("6.None")
        # print()
        choice = i
        print(choice)
        if choice>=0 and i<=6:
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

            elif choice == 5:
                points = game.defunctcoin()
                gameplayers.changescore(player,points)
                gameplayers.changefoulcount(player)
                gameplayers.nocoinspocketed(player)

            elif choice == 6:
                gameplayers.nocoinspocketed(player)

            gameplayers.showleaderboard()
            if gameplayers.checkscore()==1 or gameplayers.checkscore()==2:
                result = gameplayers.showWinner()
                return result
                # break
            elif game.coinchecker():
                print("Coins Exhausted!") 
                result = gameplayers.checkscore()
                return result
                # break
        else:
            player=player-1
            print("Unexpected input! Please try again!!")

def main():
    print("Welcome to Clean Strike Carrom Game!")
    print(playgame())

if __name__ == "__main__":
    main()
