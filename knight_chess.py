import math


class KnightChess:
    MOVE_ACTIONS = {
        1: (1, 2),
        2: (2, 1),
        3: (2, -1),
        4: (1, -2),
        5: (-1, -2),
        6: (-2, -1),
        7: (-2, 1),
        8: (-1, 2)
    }

    @classmethod
    def move(cls, starting_point, move_type):
        action = cls.MOVE_ACTIONS[move_type]
        return (starting_point[0] + action[0], starting_point[1] + action[1])

    @classmethod
    def _distance_from_start(cls, point):
        return math.sqrt(point[0] ** 2 + point[1] ** 2)
