class MarkerSelectionPlayerOne:

    def __init__(self):
        pass

    def select_marker(self):
        marker_selection_playerone = None

        while marker_selection_playerone is None:
            #  allow user to select either X or O when playing against computer
            print "Player 1 please choose your marker from A-Z:"
            marker_selection_playerone = raw_input()

            if marker_selection_playerone.isalpha() and len(marker_selection_playerone) == 1:
                player_one = marker_selection_playerone
                return player_one

            else:
                print "Please choose any marker from A-Z:"
                marker_selection_playerone = None