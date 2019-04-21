from enum import Enum

class Player(Enum):

    X = 1
    O = 2

    @property
    def other(self):
        return Player.O if self == Player.X else Player.X