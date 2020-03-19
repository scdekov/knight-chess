import math


class KnightChess:
    MOVE_ACTIONS = {
        '1': (1, 2),
        '2': (2, 1),
        '3': (2, -1),
        '4': (1, -2),
        '5': (-1, -2),
        '6': (-2, -1),
        '7': (-2, 1),
        '8': (-1, 2)
    }

    @classmethod
    def solve(cls, moves):
        furthest_point = (0, 0)
        furthest_distance = 0
        same_x_y_points = set()

        position = (0, 0)
        for move in moves:
            position = cls._move(position, move)
            if position[0] == position[1]:
                same_x_y_points.add(position)

            distance_from_start = cls._distance_from_start(position)
            if distance_from_start > furthest_distance:
                furthest_point = position
                furthest_distance = distance_from_start

        return {
            'end_position': position,
            'furthest_point': furthest_point,
            'same_x_y_points': list(same_x_y_points)
        }

    @classmethod
    def _move(cls, starting_point, move_type):
        action = cls.MOVE_ACTIONS[move_type]
        return (starting_point[0] + action[0], starting_point[1] + action[1])

    @staticmethod
    def _distance_from_start(point):
        return math.sqrt(point[0] ** 2 + point[1] ** 2)
