import numpy as np

import chess
from chess import Pawn, Bishop, Knight, Rook, Queen, King


class Game:
    def __init__(self):
        self.board = np.empty(shape=(8, 8), dtype=chess.Chess)
        for i in range(2):
            for j in range(8):
                if i == 0:
                    if j == 0 or j == 7:
                        self.board[i, j] = Rook()
                    elif j == 1 or j == 6:
                        self.board[i, j] = Knight()
                    elif j == 2 or j == 5:
                        self.board[i, j] = Bishop()
                    elif j == 3:
                        self.board[i, j] = Queen()
                    elif j == 4:
                        self.board[i, j] = King()
                else:
                    self.board[i, j] = Pawn()

        for i in range(7, 5, -1):
            for j in range(8):
                if i == 7:
                    if j == 0 or j == 7:
                        self.board[i, j] = Rook()
                    elif j == 1 or j == 6:
                        self.board[i, j] = Knight()
                    elif j == 2 or j == 5:
                        self.board[i, j] = Bishop()
                    elif j == 3:
                        self.board[i, j] = Queen()
                    elif j == 4:
                        self.board[i, j] = King()
                else:
                    self.board[i, j] = Pawn()

    def print_board(self):
        print(self.board)

if __name__ == '__main__':
    game = Game()
    game.print_board()
