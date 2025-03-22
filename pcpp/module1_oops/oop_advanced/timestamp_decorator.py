import datetime


def execution_monitor(own_function):
    def wrapper(*args):
        print(f"{own_function.__name__} execution started at {datetime.datetime.now().strftime("%Y-%M-%d %H:%m:%S.%f")}")
        own_function(*args)
        print(f"{own_function.__name__} execution finished at {datetime.datetime.now().strftime("%Y-%M-%d %H:%m:%S.%f")}")

    return wrapper


@execution_monitor
def add_numbers(num1, num2):
    print(f"The addition of {num1} and {num2} is {num1 + num2}")


@execution_monitor
def multiply_numbers(num1, num2):
    print(f"The multiplication of {num1} and {num2} is {num1 * num2}")


add_numbers(1000000, 2000000)
multiply_numbers(1000, 3000)
