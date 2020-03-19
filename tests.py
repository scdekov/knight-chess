from knight_chess import KnightChess


class TestKnightChess:
    def test_solve(self):
        assert KnightChess.solve('123') == {
            'end_position': (5, 2),
            'furthest_point': (5, 2),
            'same_x_y_points': [(3, 3)]
        }

    def test_solve__no_moves(self):
        assert KnightChess.solve('') == {
            'end_position': (0, 0),
            'furthest_point': (0, 0),
            'same_x_y_points': []
        }

    def test_solve__multiple_same_x_y_points(self):
        assert KnightChess.solve('121237') == {
            'end_position': (6, 6),
            'furthest_point': (8, 5),
            'same_x_y_points': [(3, 3), (6, 6)]
        }

    def test_move(self):
        assert KnightChess._move((0, 0), '1') == (1, 2)
        assert KnightChess._move((1, 2), '1') == (2, 4)
        assert KnightChess._move((2, 4), '1') == (3, 6)

        assert KnightChess._move((0, 0), '1') == (1, 2)
        assert KnightChess._move((1, 2), '2') == (3, 3)
        assert KnightChess._move((3, 3), '3') == (5, 2)

        assert KnightChess._move((0, 0), '1') == (1, 2)
        assert KnightChess._move((1, 2), '5') == (0, 0)

        assert KnightChess._move((0, 0), '5') == (-1, -2)
        assert KnightChess._move((-1, -2), '6') == (-3, -3)

    def test_distance_from_start(self):
        assert KnightChess._distance_from_start((3, 4)) == 5
        assert KnightChess._distance_from_start((4, 3)) == 5
        assert KnightChess._distance_from_start((6, 8)) == 10
        assert KnightChess._distance_from_start((15, 8)) == 17
