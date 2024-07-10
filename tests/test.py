import pytest
from app.calculator import Calculator


class TestCalc:
    def setup_method(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_adding_unsuccess(self):
        assert self.calc.adding(self, 1, 1) != 3

    def test_multiply_success(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_neg_multiply_success(self):
        assert self.calc.multiply(self, -2, -5) == 10

    def test_squared_success(self):
        assert self.calc.squared(self, 5) == 25

    def test_neg_squared_success(self):
        assert self.calc.squared(self, -3) == 9

    def test_division_success(self):
        assert self.calc.division(self, 2, 2) == 1

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 3, 2) == 1

    def test_neg_subtraction_success(self):
        assert self.calc.subtraction(self, -10, -20) == 10
