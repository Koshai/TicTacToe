class MarkerSelectionPlayerTwo:

    def __init__(self):
        pass

    def select_marker(self):
        marker_selection_playertwo = None

        while marker_selection_playertwo is None:
            #  allow user to select either X or O when playing against computer
            print "Player 2 please choose your marker from A-Z:"
            marker_selection_playertwo = raw_input()

            if marker_selection_playertwo.isalpha() and len(marker_selection_playertwo) == 1:
                player_two = marker_selection_playertwo
                return player_two

            else:
                print "Please choose any marker from A-Z:"
                marker_selection_playertwo = None
