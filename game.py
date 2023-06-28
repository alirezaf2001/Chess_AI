import numpy as np
from copy import deepcopy
import chess
from chess import Pawn, Bishop, Knight, Rook, Queen, King


class Game:
    def __init__(self):
        self.board = np.empty(shape=(8, 8), dtype=chess.Chess)
        for i in range(2):
            for j in range(8):
                if i == 0:
                    if j == 0 or j == 7:
                        self.board[i, j] = Rook((i, j), "black")
                    elif j == 1 or j == 6:
                        self.board[i, j] = Knight((i, j), "black")
                    elif j == 2 or j == 5:
                        self.board[i, j] = Bishop((i, j), "black")
                    elif j == 3:
                        self.board[i, j] = Queen((i, j), "black")
                    elif j == 4:
                        self.board[i, j] = King((i, j), "black")
                else:
                    self.board[i, j] = Pawn((i, j), "black")

        for i in range(7, 5, -1):
            for j in range(8):
                if i == 7:
                    if j == 0 or j == 7:
                        self.board[i, j] = Rook((i, j), "white")
                    elif j == 1 or j == 6:
                        self.board[i, j] = Knight((i, j), "white")
                    elif j == 2 or j == 5:
                        self.board[i, j] = Bishop((i, j), "white")
                    elif j == 3:
                        self.board[i, j] = Queen((i, j), "white")
                    elif j == 4:
                        self.board[i, j] = King((i, j), "white")
                else:
                    self.board[i, j] = Pawn((i, j), "white")

    def update_board(self, origin):
        new_loc = (self.board[origin[1], origin[0]].x, self.board[origin[1], origin[0]].y)
        self.board[new_loc[0], new_loc[1]] = self.board[origin[1], origin[0]]
        self.board[origin[1], origin[0]] = None

    def print_board(self):
        print(self.board)

if __name__ == '__main__':
    game = Game()
    game.print_board()
    game.board[0, 0].move((5, 5))
    game.update_board((0, 0))
    game.print_board()

