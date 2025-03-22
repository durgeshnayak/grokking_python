class WarehouseDecorator:
    def __init__(self, material):
        self.material = material

    def __call__(self, our_function):
        def wrapper(*args):
            print(f"Wrapping items from {our_function.__name__} with {self.material}")
            our_function(*args)
            print("Decorator function signing off")
            print()

        return wrapper


@WarehouseDecorator('kraft')
def pack_books(*args):
    print("We'll pack books:", args)


@WarehouseDecorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)


@WarehouseDecorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)


pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')
