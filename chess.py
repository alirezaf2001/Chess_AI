class Chess:
    def __init__(self,location , white):
        self.location = location
        self.white = white

    def move(self, destination):
        pass

class Pawn(Chess):
    """
    Pawn can only move forward and attack forward-diagonally
    """
    def __init__(self):
        pass

    def __repr__(self):
        return 'P'

class Bishop(Chess):
    """
    Bishop can only move diagonally
    """
    def __init__(self):
        pass

    def __repr__(self):
        return 'B'

class Knight(Chess):
    """
    Knight can only move in L shape and can jump pieces
    """
    def __init__(self):
        pass

    def __repr__(self):
        return 'K'


class Rook(Chess):
    """
    Rook can only move in straight line
    """
    def __init__(self):
        pass

    def __repr__(self):
        return 'R'


class Queen(Chess):
    """
    Queen can move in straight lines or diagonally
    """
    def __init__(self):
        pass

    def __repr__(self):
        return 'Q'


class King(Chess):
    """
    King can only move one space in each direction
    """
    def __init__(self):
        pass

    def __repr__(self):
        return 'K'
