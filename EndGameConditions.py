class EndGameConditions:

    def __init__(self):
        pass

    def three_in_a_row(self, player_one, player_two, *args):
        return args[0] == args[1] == args[2] == player_one or \
               args[0] == args[1] == args[2] == player_two

    def game_is_over(self, player_one, player_two, b):
        return self.three_in_a_row(player_one, player_two, b[0], b[1], b[2]) == 1 or \
               self.three_in_a_row(player_one, player_two, b[3], b[4], b[5]) == 1 or \
               self.three_in_a_row(player_one, player_two, b[6], b[7], b[8]) == 1 or \
               self.three_in_a_row(player_one, player_two, b[0], b[3], b[6]) == 1 or \
               self.three_in_a_row(player_one, player_two, b[1], b[4], b[7]) == 1 or \
               self.three_in_a_row(player_one, player_two, b[2], b[5], b[8]) == 1 or \
               self.three_in_a_row(player_one, player_two, b[0], b[4], b[8]) == 1 or \
               self.three_in_a_row(player_one, player_two, b[2], b[4], b[6]) == 1