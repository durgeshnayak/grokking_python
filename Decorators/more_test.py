"""Tests for more advanced decorator exercises"""
import math
import unittest

from more import (
    coalesce_all,
    lazy_repr,
    positional_only,
    at,
)


class CoalesceAllTests(unittest.TestCase):

    """Tests for coalesce_all."""

    def test_coalesce_one_argument(self):
        @coalesce_all("world")
        def greet(greet="world"):
            return "Hello {}".format(greet)
        self.assertEqual(greet("Trey"), "Hello Trey")
        self.assertEqual(greet("someone"), "Hello someone")
        self.assertEqual(greet(""), "Hello ")
        self.assertEqual(greet(None), "Hello world")
        self.assertEqual(greet(), "Hello world")

    def test_coalesce_one_argument_from_empty_string(self):
        @coalesce_all("world", sentinel="")
        def greet(greet="world"):
            return "Hello {}".format(greet)
        self.assertEqual(greet("Trey"), "Hello Trey")
        self.assertEqual(greet("someone"), "Hello someone")
        self.assertEqual(greet(""), "Hello world")
        self.assertEqual(greet(None), "Hello None")
        self.assertEqual(greet(), "Hello world")

    def test_coalesce_multiple_arguments(self):
        @coalesce_all(1)
        def multiply(x, y):
            return x * y
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(None, None), 1)
        self.assertEqual(multiply(2, None), 2)
        self.assertEqual(multiply(None, 3), 3)
        with self.assertRaises(TypeError):
            multiply(4)
        with self.assertRaises(TypeError):
            multiply()

    def test_coalesce_keyword_arguments(self):
        @coalesce_all(1)
        def multiply(x, y):
            return x * y
        self.assertEqual(multiply(x=2, y=3), 6)
        self.assertEqual(multiply(2, y=3), 6)
        self.assertEqual(multiply(x=None, y=None), 1)
        self.assertEqual(multiply(x=2, y=None), 2)
        self.assertEqual(multiply(2, y=None), 2)
        self.assertEqual(multiply(x=None, y=3), 3)
        self.assertEqual(multiply(None, y=3), 3)
        with self.assertRaises(TypeError):
            multiply(x=4)
        with self.assertRaises(TypeError):
            multiply(y=4)


class LazyReprTests(unittest.TestCase):

    """Tests for lazy_repr."""

    def test_with_concrete_attributes(self):
        @lazy_repr
        class Point:
            def __init__(self, x, y, z):
                self.x, self.y, self.z = x, y, z
        self.assertEqual(str(Point(1, 2, 3)), "Point(x=1, y=2, z=3)")
        self.assertEqual(repr(Point(x=3, y=4, z=5)), "Point(x=3, y=4, z=5)")

    def test_argument_without_an_attribute(self):
        @lazy_repr
        class BankAccount:
            def __init__(self, opening_balance):
                self.balance = opening_balance

        self.assertEqual(str(BankAccount(10)), "BankAccount(balance=10)")
        self.assertEqual(repr(BankAccount(10)), "BankAccount(balance=10)")


class PositionalOnlyTests(unittest.TestCase):

    """Tests for positional_only."""

    def test_restrict_all_arguments_to_positional(self):
        @positional_only
        def divide(x, y): return x / y
        self.assertEqual(divide(21, 3), 7)
        self.assertEqual(divide(5, 2), 2.5)
        with self.assertRaises(TypeError):
            divide(x=5, y=2)
        with self.assertRaises(TypeError):
            divide(5, y=2)
        with self.assertRaises(TypeError):
            divide(5, x=2)
        with self.assertRaises(TypeError):
            divide(1, 2, 3)
        with self.assertRaises(TypeError):
            divide(1)

    def test_no_keyword_arguments_allowed(self):
        @positional_only
        def my_func(a, b=2, **kwargs): return a
        self.assertEqual(my_func(3), 3)
        with self.assertRaises(TypeError):
            my_func(3, b=3)
        with self.assertRaises(TypeError):
            my_func(3, a=3)

    def test_any_number_of_positional_arguments(self):
        @positional_only
        def add(a, b, *args): return a + b + sum(args)
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, 2, 3, 4), 10)
        self.assertEqual(add(1, 2, 3), 6)
        @positional_only
        def product(*numbers):
            total = 1
            for n in numbers:
                total *= n
            return total
        self.assertEqual(product(1, 2, 3, 4), 24)
        self.assertEqual(product(1, 2), 2)
        self.assertEqual(product(10), 10)
        self.assertEqual(product(), 1)
        with self.assertRaises(TypeError):
            add(1, 2, b=3)
        with self.assertRaises(TypeError):
            product(numbers=3)

    def test_with_positional_argument_count(self):
        @positional_only(3)
        def add(a, b, c, d): return a + b + c + d
        self.assertEqual(add(1, 2, 3, 4), 10)
        self.assertEqual(add(1, 2, 3, d=4), 10)
        with self.assertRaises(TypeError):
            add(1, 2, c=3, d=4)
        with self.assertRaises(TypeError):
            add(1, b=2, c=3, d=4)
        with self.assertRaises(TypeError):
            add(a=1, b=2, c=3, d=4)
        @positional_only(2)
        def divide(x=1, y=1): return x / y
        self.assertEqual(divide(3, 2), 1.5)
        with self.assertRaises(TypeError):
            divide(x=3, y=2)
        with self.assertRaises(TypeError):
            divide(3, y=2)


class AtTests(unittest.TestCase):

    """Tests for at."""

    def test_one_decorator(self):
        @at(reprify)
        def add(x, y):
            return x + y
        self.assertEqual(add(1, 2), '3')
        self.assertEqual(add(1, 3), '4')
        self.assertEqual(add(x=2, y=3), '5')

    def test_two_decorators(self):
        @at(sqrtd, reprify)
        def add(x, y):
            return x + y
        self.assertEqual(add(1, 3), '2.0')
        self.assertEqual(add(x=20, y=5), '5.0')

        @at(sqrtd, of_squares)
        def add(x, y):
            return x + y
        self.assertEqual(add(3, 4), 5)
        self.assertEqual(add(8, 15), 17)

    def test_three_decorators(self):
        @at(sqrtd, of_squares, reprify)
        def add(x, y):
            return x + y
        self.assertEqual(add(3, 4), '5.0')
        self.assertEqual(add(8, 15), '17.0')


def reprify(func):
    def wrapper(*args, **kwargs):
        return repr(func(*args, **kwargs))
    return wrapper


def sqrtd(func):
    def wrapper(*args, **kwargs):
        return math.sqrt(func(*args, **kwargs))
    return wrapper


def of_squares(func):
    def wrapper(*args, **kwargs):
        args = (n**2 for n in args)
        kwargs = {k: v**2 for k, v in kwargs.items()}
        return func(*args, **kwargs)
    return wrapper


if __name__ == "__main__":
    from helpers import error_message
    error_message()
