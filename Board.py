class Board:

    def __init__(self):
        pass

    def show_board(self, board):

        # Show the current board status
        status = " %s | %s | %s \n===+===+===\n %s | %s | %s \n===+===+===\n %s | %s | %s \n" % \
                 (board[0], board[1], board[2],
                  board[3], board[4], board[5],
                  board[6], board[7], board[8])

        print status

        return status