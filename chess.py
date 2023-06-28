class Chess:
    def __init__(self, location, color):
        self.x = location[0]
        self.y = location[1]
        self.color = color

    def validate_movement(self):
        pass

    def move(self, destination):
        if self.validate_movement(destination):
            self.x = destination[1]
            self.y = destination[0]
            return True
        else:
            return False


class Pawn(Chess):
    """
    Pawn can only move forward and attack forward-diagonally
    """
    def __init__(self, location, color):
        super().__init__(location, color)
        self.first_move = True

    def validate_movement(self, destination):
        # TODO: Finish pawn movement validation
        if self.color == "white":
            if self.first_move:
                if 0 < self.x - destination[1] <= 2 and self.y == destination[0]:
                    return True
            else:
                if self.x - destination[1] == 1 and self.y == destination[0]:
                    return True
        else:
            if self.first_move:
                if 0 < destination[1] - self.x <= 2 and self.y == destination[0]:
                    return True
            else:
                if destination[1] - self.x == 1 and self.y == destination[0]:
                    return True
        return False

    def move(self, destination):
        if self.validate_movement(destination):
            self.x = destination[1]
            self.y = destination[0]
            self.first_move = False
            return True
        else:
            return False

    def __repr__(self):
        return 'P'

class Bishop(Chess):
    """
    Bishop can only move diagonally
    """
    def validate_movement(self, destination):
        return True

    def __repr__(self):
        return 'B'

class Knight(Chess):
    """
    Knight can only move in L shape and can jump pieces
    """
    def validate_movement(self, destination):
        return True

    def __repr__(self):
        return 'K'


class Rook(Chess):
    """
    Rook can only move in straight line
    """
    def validate_movement(self, destination):
        return True

    def __repr__(self):
        return 'R'


class Queen(Chess):
    """
    Queen can move in straight lines or diagonally
    """
    def validate_movement(self, destination):
        return True

    def __repr__(self):
        return 'Q'


class King(Chess):
    """
    King can only move one space in each direction
    """
    def validate_movement(self, destination):
        return True

    def __repr__(self):
        return 'KING'
