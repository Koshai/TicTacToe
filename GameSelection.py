class GameSelection:

    def __init__(self):
        pass

    def game_selection(self):
        # Allow selection of the type of game
        print "Please select how you want to play the game:\n" \
              "1 - Player vs Computer\n" \
              "2 - Player vs Player\n" \
              "3 - Computer vs Computer"

        play = None

        while play is None:
            try:
                play = int(raw_input())
            except:
                print "Please enter correct input from 1-3:"

            if play == 1 or play == 2 or play == 3:
                return play

            else:
                play = None