def simple_decorator(our_function):
    def wrapper(*args):
        print(f"Decorating {our_function.__name__} and calling it with args: {args}")
        our_function(*args)
        print("Decorator function signing off...")

    return wrapper


@simple_decorator
def my_function(*args):
    print(f"My function called with args: {args}")


my_function("Durgesh", "Snehal", "Chinmayee")