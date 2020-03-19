from knight_chess import KnightChess


class TestKnightChess:
    def test_move(self):
        assert KnightChess.move((0, 0), 1) == (1, 2)
        assert KnightChess.move((1, 2), 1) == (2, 4)
        assert KnightChess.move((2, 4), 1) == (3, 6)

        assert KnightChess.move((0, 0), 1) == (1, 2)
        assert KnightChess.move((1, 2), 2) == (3, 3)
        assert KnightChess.move((3, 3), 3) == (5, 2)

        assert KnightChess.move((0, 0), 1) == (1, 2)
        assert KnightChess.move((1, 2), 5) == (0, 0)

        assert KnightChess.move((0, 0), 5) == (-1, -2)
        assert KnightChess.move((-1, -2), 6) == (-3, -3)
