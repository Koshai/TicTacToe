class Tie:
    def __init__(self):
        pass

    def tie(self, player_one, player_two, b):
        return len([s for s in b if s == player_one or s == player_two]) == 9