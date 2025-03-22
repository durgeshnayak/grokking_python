"""Function object exercises"""


def call(function, *args, **kwargs):
    """Call the function provided with the given arguments."""
    function(*args, **kwargs)


def call_later():
    """Return a function to call given function with provided arguments."""
    def wrapper(function, *args, **kwargs):
        return function(*args, **kwargs)
    return wrapper


def exclude():
    """Only keep items which fail a given predicate test"""


def call_logger():
    """Return a new function that calls func and prints when it was called."""


def call_again():
    """Return function return value and a function to call again."""


def only_once():
    """Return new version of the function that can only be called once."""
