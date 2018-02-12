from EndGameConditions import EndGameConditions
from HumanMove import HumanMove
from ComputerMove import ComputerMove
from Board import Board
from Tie import Tie

class PlayerSecondVsComputerFirst:

    def __init__(self, player_one, player_two, board):
        self.player_one = player_one
        self.player_two = player_two

        self.board = board

        self.playersecond_vs_computerfirst(self.player_one, self.player_two, self.board)

    def playersecond_vs_computerfirst(self, player_one, player_two, board):

      # start by giving a message
      print "Computer makes the first move."

      # start by printing the board
      Board().show_board(board)

      # loop through until the game was won or tied
      while not EndGameConditions().game_is_over(player_one, player_two, board) and not Tie().tie(player_one, player_two, board):
        if not EndGameConditions().game_is_over(player_one, player_two, board) and not Tie().tie(player_one, player_two, board):
          ComputerMove().eval_board(player_two, player_one, board)

          if EndGameConditions().game_is_over(player_one, player_two, board):
            Board().show_board(board)
            print "Computer wins!"
            return True

        Board().show_board(board)

        if not EndGameConditions().game_is_over(player_one, player_two, board) and not Tie().tie(player_one, player_two, board):
          HumanMove().get_human_spot(player_one, board)

          if EndGameConditions().game_is_over(player_one, player_two, board):
            Board().show_board(board)
            print "Player " + player_one + " wins!"
            return True

      if Tie().tie(player_one, player_two, board) and not EndGameConditions().game_is_over(player_one, player_two, board):
        print "The game is a tie"
        return True