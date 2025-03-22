"""Tests for decorator exercises"""
from contextlib import redirect_stdout
from io import StringIO
import unittest

from decorators import (
    count_calls,
    jsonify,
    groot,
    four,
    record_calls,
)


class CountCallsTests(unittest.TestCase):

    """Test for count_calls."""

    def test_accepts_a_function(self):
        # Function value is returned
        def one(): return 1
        decorated = count_calls(one)
        self.assertEqual(decorated(), 1)
        self.assertEqual(decorated.calls, 1)

    def test_calls_a_function(self):
        # Function is called each time
        recordings = []
        def my_func():
            recordings.append('call')
            return recordings
        decorated = count_calls(my_func)
        self.assertEqual(recordings, [])
        self.assertEqual(decorated.calls, 0)
        self.assertEqual(decorated(), ['call'])
        self.assertEqual(decorated.calls, 1)
        self.assertEqual(decorated(), ['call', 'call'])
        self.assertEqual(decorated.calls, 2)

    def test_accepts_arguments(self):
        # Function accepts positional arguments
        @count_calls
        def add(x, y):
            return x + y
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, 3), 4)

        # Function accepts keyword arguments
        recordings = []
        @count_calls
        def my_func(*args, **kwargs):
            recordings.append((args, kwargs))
            return recordings
        self.assertEqual(my_func(), [((), {})])
        self.assertEqual(my_func(1, 2, a=3), [((), {}), ((1, 2), {'a': 3})])

        # Exceptions are still counted as calls
        @count_calls
        def my_func():
            raise AssertionError("Function called too soon")
        self.assertEqual(my_func.calls, 0)
        with self.assertRaises(AssertionError):
            my_func()
        self.assertEqual(my_func.calls, 1)
        self.assertEqual(my_func.calls, 1)
        with self.assertRaises(AssertionError):
            my_func()
        self.assertEqual(my_func.calls, 2)


class JSONifyTests(unittest.TestCase):

    """Tests for jsonify."""

    def test_serialize_none(self):
        func = jsonify(lambda: None)
        self.assertEqual(func(), 'null')

    def test_serialize_list(self):
        def make_list(): return [4, 'hi', True, 5.5]
        make_list = jsonify(make_list)
        self.assertEqual(make_list(), '[4, "hi", true, 5.5]')

    def test_returned(self):
        def return_hi(): return 'hi'
        return_hi = jsonify(return_hi)
        self.assertEqual(return_hi(), '"hi"')

    def test_takes_arguments(self):
        def add(x, y): return x + y
        add = jsonify(add)
        self.assertEqual(add(1, 2), '3')
        self.assertEqual(add(x=1, y=2), '3')


class GrootTests(unittest.TestCase):

    """Tests for groot."""

    def test_print_groot(self):
        def greet(name): print("Hello {}".format(name))
        greet = groot(greet)
        with redirect_stdout(StringIO()) as stdout:
            greet("Trey")
        self.assertEqual(stdout.getvalue(), "Groot\n")

    def test_nothing_returned(self):
        def return_hi(): return 'hi'
        return_hi = groot(return_hi)
        with redirect_stdout(StringIO()) as stdout:
            self.assertEqual(return_hi(), None)

    def test_function_ignored(self):
        def return_hi(): dictionary['key'] = 'value'
        dictionary = {}
        return_hi = groot(return_hi)
        with redirect_stdout(StringIO()) as stdout:
            self.assertEqual(return_hi(), None)
        self.assertEqual(dictionary, {})

    def test_takes_arguments(self):
        def add(x, y): return x + y
        add = groot(add)
        with redirect_stdout(StringIO()) as stdout:
            add(1, 2)
            add(x=1, y=2)


class FourTests(unittest.TestCase):

    """Tests for four."""

    def test_return_four(self):
        def greet(name): print("Hello {}".format(name))
        with redirect_stdout(StringIO()) as stdout:
            greet = four(greet)
        self.assertEqual(stdout.getvalue(), '')
        self.assertEqual(greet, 4)


class RecordCallsTests(unittest.TestCase):

    """Tests for record_calls."""

    def test_call_count_starts_at_zero(self):
        decorated = record_calls(lambda: None)
        self.assertEqual(decorated.call_count, 0)

    def test_not_called_on_decoration_time(self):
        def my_func():
            raise AssertionError("Function called too soon")
        record_calls(my_func)

    def test_function_still_callable(self):
        recordings = []
        def my_func():
            recordings.append('call')
        decorated = record_calls(my_func)
        self.assertEqual(recordings, [])
        decorated()
        self.assertEqual(recordings, ['call'])
        decorated()
        self.assertEqual(recordings, ['call', 'call'])

    def test_return_value(self):
        def one(): return 1
        one = record_calls(one)
        self.assertEqual(one(), 1)

    def test_takes_arguments(self):
        def add(x, y): return x + y
        add = record_calls(add)
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, 3), 4)

    def test_takes_keyword_arguments(self):
        recordings = []
        @record_calls
        def my_func(*args, **kwargs):
            recordings.append((args, kwargs))
            return recordings
        self.assertEqual(my_func(), [((), {})])
        self.assertEqual(my_func(1, 2, a=3), [((), {}), ((1, 2), {'a': 3})])

    def test_call_count_increments(self):
        decorated = record_calls(lambda: None)
        self.assertEqual(decorated.call_count, 0)
        decorated()
        self.assertEqual(decorated.call_count, 1)
        decorated()
        self.assertEqual(decorated.call_count, 2)

    def test_different_functions(self):
        my_func1 = record_calls(lambda: None)
        my_func2 = record_calls(lambda: None)
        my_func1()
        self.assertEqual(my_func1.call_count, 1)
        self.assertEqual(my_func2.call_count, 0)
        my_func2()
        self.assertEqual(my_func1.call_count, 1)
        self.assertEqual(my_func2.call_count, 1)

    def test_docstring_and_name_preserved(self):
        import pydoc
        decorated = record_calls(example)
        self.assertIn('function example', str(decorated))
        documentation = pydoc.render_doc(decorated)
        self.assertIn('function example', documentation)
        self.assertIn('Example function.', documentation)
        self.assertIn('(a, b=True)', documentation)

    def test_record_arguments(self):
        @record_calls
        def my_func(*args, **kwargs): return args, kwargs
        self.assertEqual(my_func.calls, [])
        my_func()
        self.assertEqual(len(my_func.calls), 1)
        self.assertEqual(my_func.calls[0].args, ())
        self.assertEqual(my_func.calls[0].kwargs, {})
        my_func(1, 2, a=3)
        self.assertEqual(len(my_func.calls), 2)
        self.assertEqual(my_func.calls[1].args, (1, 2))
        self.assertEqual(my_func.calls[1].kwargs, {'a': 3})

    def test_record_return_values(self):
        from decorators import NO_RETURN
        @record_calls
        def my_func(*args, **kwargs): return sum(args), kwargs
        my_func()
        self.assertEqual(my_func.calls[0].return_value, (0, {}))
        my_func(1, 2, a=3)
        self.assertEqual(my_func.calls[1].return_value, (3, {'a': 3}))
        self.assertIs(my_func.calls[1].exception, None)
        with self.assertRaises(TypeError) as context:
            my_func(1, 'hi', a=3)
        self.assertIs(my_func.calls[2].return_value, NO_RETURN)
        self.assertEqual(my_func.calls[2].exception, context.exception)


def example(a, b=True):
    """Example function."""
    print('hello world')


if __name__ == "__main__":
    from helpers import error_message
    error_message()
