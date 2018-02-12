from MarkerSelectionPlayerOne import MarkerSelectionPlayerOne
from MarkerSelectionPlayerTwo import MarkerSelectionPlayerTwo
from GameSelection import GameSelection
from PlayerVsPlayer import PlayerVsPlayer
from PlayerFirstVsComputerSecond import PlayerFirstVsComputerSecond
from PlayerSecondVsComputerFirst import PlayerSecondVsComputerFirst
from ComputerVsComputer import ComputerVsComputer
from FirstPlay import FirstPlay

class Game:
  def __init__(self):
      # Greet the user
      print "Welcome to Tic Tac Toe"

      self.player_one = ""  # First Player Marker
      self.player_two = ""  # Second Player Marker

      self.play = 0  # The Number represents game mode

      self.play_order = ""  # This should be either Y or N and stores the value whether player will go first or not

      self.board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

      # Allow player to select custom marker
      self.player_one = MarkerSelectionPlayerOne().select_marker()
      self.player_two = MarkerSelectionPlayerTwo().select_marker()

      #Select the game mode
      self.play = GameSelection().game_selection()

      if self.play == 1:
          self.play_order = FirstPlay().first_play()
          if self.play_order == "Y":
            PlayerFirstVsComputerSecond(self.player_one, self.player_two, self.board)
          else:
            PlayerSecondVsComputerFirst(self.player_one, self.player_two, self.board)
      elif self.play == 2:
          PlayerVsPlayer(self.player_one, self.player_two, self.board)
      elif self.play == 3:
          ComputerVsComputer(self.player_one, self.player_two, self.board)

if __name__ == '__main__':
  game = Game()