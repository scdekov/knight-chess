from collections import OrderedDict
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
        start_position = (0, 0)
        furthest_points = OrderedDict({start_position: 1})
        furthest_distance = 0
        same_x_y_points = OrderedDict()

        position = start_position
        for move in moves:
            position = cls._move(position, move)
            if position[0] == position[1] and position != start_position:
                same_x_y_points[position] = 1

            distance_from_start = cls._distance_from_start(position)
            if distance_from_start > furthest_distance:
                furthest_points = OrderedDict({position: 1})
                furthest_distance = distance_from_start
            elif distance_from_start == furthest_distance:
                furthest_points[position] = 1

        return {
            'end_position': position,
            'furthest_points': list(furthest_points.keys()),
            'same_x_y_points': list(same_x_y_points.keys())
        }

    @classmethod
    def _move(cls, starting_point, move_type):
        action = cls.MOVE_ACTIONS[move_type]
        return (starting_point[0] + action[0], starting_point[1] + action[1])

    @staticmethod
    def _distance_from_start(point):
        return math.sqrt(point[0] ** 2 + point[1] ** 2)
