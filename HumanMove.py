class HumanMove:
    def __init__(self):
        pass

    def get_human_spot(self, input, board):
        # Take input from human player
        print "Please enter from 0-8:"
        spot = None
        while spot is None:
            # loop until the user enters an integer number
            try:
                spot = int(raw_input())
            except ValueError:
                print "Please enter correct input from 0-8:"
                spot = None
            if spot in [0, 1, 2, 3, 4, 5, 6, 7, 8]:  # validate until user enters the number from 0-8
                if board[spot].isalpha() == False:
                    board[spot] = input
                    return "Taken"  # The return is used for testing purposes
                else:
                    print "This spot is taken. Please choose another:"
                    spot = None
            else:
                print "Please enter correct input from 0-8:"
                spot = None