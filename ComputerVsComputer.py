from EndGameConditions import EndGameConditions
from ComputerMove import ComputerMove
from Board import Board
from Tie import Tie

class ComputerVsComputer:

    def __init__(self, player_one, player_two, board):
        self.player_one = player_one
        self.player_two = player_two

        self.board = board

        self.computer_vs_computer(self.player_one, self.player_two, self.board)

    def computer_vs_computer(self, player_one, player_two, board):
        # start by giving a message
        print "Computer " + player_one + " makes the first move"
        # start by printing the board
        Board().show_board(board)

        # loop through until the game was won or tied
        while not EndGameConditions().game_is_over(player_one, player_two, board) and not Tie().tie(player_one, player_two, board):
            if not EndGameConditions().game_is_over(player_one, player_two, board) and not Tie().tie(player_one, player_two, board):
                ComputerMove().eval_board(player_one, player_two, board)

                if EndGameConditions().game_is_over(player_one, player_two, board):
                    Board().show_board(Board)
                    print "Computer 1 wins!"
                    return True

            Board().show_board(board)

            if not EndGameConditions().game_is_over(player_one, player_two, board) and not Tie().tie(player_one, player_two, board):
                ComputerMove().eval_board(player_two, player_one, board)

                if EndGameConditions().game_is_over(player_one, player_two, board):
                    Board().show_board(Board)
                    print "Computer 2 wins!"
                    return True

            Board().show_board(board)

            if Tie().tie(player_one, player_two, board) and not EndGameConditions().game_is_over(player_one, player_two, board):
                print "The game is a tie"
                return True