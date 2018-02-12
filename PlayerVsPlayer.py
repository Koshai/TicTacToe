from EndGameConditions import EndGameConditions
from HumanMove import HumanMove
from Board import Board
from Tie import Tie

class PlayerVsPlayer:

    def __init__(self, player_one, player_two, board):
        self.player_one = player_one
        self.player_two = player_two

        self.board = board

        self.player_vs_player(self.player_one, self.player_two, self.board)

    def player_vs_player(self, player_one, player_two, board):

        # start by giving a message
        print "Player 1 the first move"
        # start by printing the board
        Board().show_board(board)

        # loop through until the game was won or tied
        while not EndGameConditions().game_is_over(player_one, player_two, board) and not Tie().tie(player_one, player_two, board):
            HumanMove().get_human_spot(player_one, board)

            if EndGameConditions().game_is_over(player_one, player_two, board):
                Board().show_board(board)
                print "Player " + player_one + " wins!"
                return True

            Board().show_board(board)

            if not EndGameConditions().game_is_over(player_one, player_two, board) and not Tie().tie(player_one, player_two, board):
                print "Player 2"
                HumanMove().get_human_spot(player_two, board)

                if EndGameConditions().game_is_over(player_one, player_two, board):
                    Board().show_board(board)
                    print "Player " + player_two + " wins!"
                    return True

            Board().show_board(board)

            if Tie().tie(player_one, player_two, board) and not EndGameConditions().game_is_over(player_one, player_two, board):
                print "The game is a tie"
                return True