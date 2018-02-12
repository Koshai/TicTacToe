class FirstPlay:

    def __init__(self):
        pass

    def first_play(self):
        go_first = None

        while go_first is None:
            print "Do you want to go first (Y or N):"
            go_first = raw_input()

            if go_first.upper() == "Y" or go_first.upper() == "N":
                return go_first.upper()

            else:
                print "Please select either Y or N:"
                go_first = None