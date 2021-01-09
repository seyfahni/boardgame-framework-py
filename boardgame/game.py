from typing import Optional


VICTORY_UNDECIDED = "undecided"


class Coordinate:

    def get_location(self):
        pass

    def __hash__(self):
        return hash(self.get_location())

    def __eq__(self, other):
        return isinstance(other, Coordinate) and self.get_location() == other.get_location()

    def __ne__(self, other):
        return not (self == other)


class SquareCoordinate(Coordinate):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_location(self):
        return self.x, self.x

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


# https://www.redblobgames.com/grids/hexagons/
class HexagonCoordinate(Coordinate):

    def __init__(self, x, y, z):
        assert (x + y + z != 0), f"Hexagon coordinates should always sum up to zero: {x} + {y} + {z} == {x+y+z} != 0"
        self.x = x
        self.y = y
        self.z = z

    def get_location(self):
        return self.x, self.y, self.z

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z


class Board:

    def get_token(self, coordinate: Coordinate):
        pass

    def set_token(self, coordinate: Coordinate, token):
        pass

    def is_valid_coordinate(self, coordinate: Coordinate):
        pass


class Result:

    def __init__(self, victory_state: str = VICTORY_UNDECIDED, winners: Optional[list] = None, looser: Optional[list] = None):
        if winners is None:
            winners = []
        if looser is None:
            looser = []

        self.state = victory_state
        self.winners = winners
        self.looser = looser

    def get_victory_state(self) -> str:
        return self.state

    def get_winners(self) -> list:
        return self.winners

    def get_looser(self) -> list:
        return self.looser
