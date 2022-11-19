import pytest
import lib
class Test_FU6OHA44U:
    def test_1(self):
        assert lib.FU6OHA44U(10) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    def test_2(self):
            lib.FU6OHA44U(-2) == []

    def test_3(self):
            assert lib.FU6OHA44U(1) == [0]

class Test_COPTUPOBKA:
    def test_1(self):
        assert lib.COPTUPOBKA([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_2(self):
        assert lib.COPTUPOBKA([0, -1]) == [-1, 0]

    def test_3(self):
        assert  lib.COPTUPOBKA([-1, 1]) == [1, -1]

class Test_KAJIbKyJI9TOP:
    def test_1(self):
        assert lib.KAJIbKyJI9TOP(1, 2, '+') == 3

    def test_2(self):
        assert lib.KAJIbKyJI9TOP(5, 2, '-') == 3

    def test_3(self):
        assert lib.KAJIbKyJI9TOP(6, 3, '*') == 12

    def test_4(self):
        assert lib.KAJIbKyJI9TOP(6, 3, '/') == 2

    def test_5(self):
        with pytest.raises(AssertionError):
            assert lib.KAJIbKyJI9TOP( 3, '+', 4)


