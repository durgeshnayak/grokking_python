def method_decoration_wrapper(function):
    def wrapper_function(*args):
        method_description = f"You called {function.__name__}("
        for arg in args:
            method_description += f"{arg},"
        method_description = method_description.rstrip(",")
        method_description += ")"
        print(method_description)
        result = function(args[0], args[1], args[2])
        print(f"It returned: {result}")

    return wrapper_function


@method_decoration_wrapper
def add(num1, num2, num3):
    return num1 + num2 + num3


add(1, 2, 3)
