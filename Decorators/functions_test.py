"""Tests for function object exercises"""
from contextlib import redirect_stdout
from io import StringIO
from textwrap import dedent
import unittest

from functions import (
    call,
    call_later,
    exclude,
    call_logger,
    call_again,
    only_once,
)


class CallTests(unittest.TestCase):

    """Tests for call."""

    def test_int_call(self):
        self.assertEqual(call(int), 0)

    def test_five_call(self):
        self.assertEqual(call(int, "5"), 5)

    def test_hello_call(self):
        self.assertEqual(call(len, "hello"), 5)

    def test_zip_call(self):
        self.assertEqual(list(call(zip, [1, 2], [3, 4])), [(1, 3), (2, 4)])


class CallLaterTests(unittest.TestCase):

    """Tests for call_later."""

    def test_append_to_list(self):
        names = []
        append_name = call_later(names.append, "Trey")
        self.assertIsNone(append_name())
        self.assertEqual(names, ['Trey'])
        append_name()
        self.assertEqual(names, ['Trey', 'Trey'])

    def test_zip_later(self):
        call_zip = call_later(zip, [1, 2], [3, 4])
        self.assertEqual(list(call_zip()), [(1, 3), (2, 4)])


class ExcludeTests(unittest.TestCase):

    """Tests for exclude."""

    def test_bool_exclude(self):
        self.assertEqual(
            exclude(bool, [False, True, False]),
            [False, False],
        )

    def test_lambda_exclude(self):
        self.assertEqual(
            exclude(lambda x: len(x) > 3, ["red", "blue", "green"]),
            ['red'],
        )


class CallLoggerTests(unittest.TestCase):

    """Tests for call_logger."""

    def test_prints_before_and_after(self):
        def greet(): print("Hello")
        greet = call_logger(greet)
        with redirect_stdout(StringIO()) as stdout:
            greet()
        self.assertEqual(stdout.getvalue(), dedent("""
            Function started
            Hello
            Function returned
        """).lstrip())

    def test_returned(self):
        def return_hi(): return 'hi'
        return_hi = call_logger(return_hi)
        with redirect_stdout(StringIO()) as stdout:
            self.assertEqual(return_hi(), 'hi')
        self.assertEqual(stdout.getvalue(), dedent("""
            Function started
            Function returned
        """).lstrip())

    def test_takes_arguments(self):
        def add(x, y): return x + y
        add = call_logger(add)
        with redirect_stdout(StringIO()) as stdout:
            self.assertEqual(add(1, 2), 3)
            self.assertEqual(add(x=1, y=2), 3)


class CallAgainTests(unittest.TestCase):

    """Tests for call_again."""

    def test_str_on_list(self):
        names = []
        response, names_as_str = call_again(str, names)
        self.assertEqual(response, '[]')
        names.append("Diane")
        self.assertEqual(names_as_str(), "['Diane']")


class OnlyOnceTests(unittest.TestCase):

    """Tests for only_once."""

    def test_do_once(self):
        def do_something(x, y):
            return x * 2 + y ** 2

        do_something_once = only_once(do_something)
        do_something_once(1, 2)
        with self.assertRaises(ValueError):
            do_something_once(1, 2)


if __name__ == "__main__":
    from helpers import error_message
    error_message()

