from EndGameConditions import EndGameConditions

class ComputerMove:
    def __init__(self):
        pass

    def eval_board(self, input, opponent_input, board):
        spot = None
        while spot is None:
            #  The computer will first attempt to reserve 4 at first try
            if board[4] == "4":
                spot = 4
                board[spot] = input
                print "Computer " + input + " has entered " + str(spot)
                return input, str(spot)
            # Preventing forks to be created by the opponent
            elif board[0] == opponent_input and board[8] == opponent_input and board[7] == "7":
                spot = 7
                board[spot] = input
                print "Computer " + input + " has entered " + str(spot)
                return input, str(spot)
            elif board[2] == opponent_input and board[6] == opponent_input and board[7] == "7":
                spot = 7
                board[spot] = input
                print "Computer " + input + " has entered " + str(spot)
                return input, str(spot)
            elif board[0] == opponent_input and board[6] == opponent_input and board[3] == "3":
                spot = 3
                board[spot] = input
                print "Computer " + input + " has entered " + str(spot)
                return input, str(spot)
            elif board[2] == opponent_input and board[8] == opponent_input and board[5] == "5":
                spot = 5
                board[spot] = input
                print "Computer " + input + " has entered " + str(spot)
                return input, str(spot)
            else:
                #  Making sure the player do not win by blocking winning opportunities
                spot = self.get_best_move(board, input, opponent_input)
                if board[spot] != input and board[spot] != opponent_input:
                    board[spot] = input
                    print "Computer " + input + " has entered " + str(spot)
                    return input, str(spot)
                else:
                    spot = None

    def get_best_move(self, board, player_one, player_two):
        available_spaces = [s for s in board if s != player_one and s != player_two]
        best_move = None

        for avail in available_spaces:
            board[int(avail)] = player_one
            if EndGameConditions().game_is_over(player_one, player_two, board):
                best_move = int(avail)
                board[int(avail)] = avail
                return best_move
            else:
                board[int(avail)] = player_two
                if EndGameConditions().game_is_over(player_one, player_two, board):
                    best_move = int(avail)
                    board[int(avail)] = avail
                    return best_move
                else:
                    board[int(avail)] = avail

        if best_move:
            return best_move
        else:
            return int(available_spaces[0])