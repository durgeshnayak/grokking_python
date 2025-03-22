class BigContainer:
    def __init__(self, material):
        self.material = material

    def __call__(self, function):
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
            print('<strong>*</strong> The whole order would be packed with', self.material)
            print()

        return wrapper


class WarehouseDecorator:
    def __init__(self, material):
        self.material = material

    def __call__(self, function):
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
            print(f'<strong>*</strong> Wrapping items from {function.__name__} with {self.material}')

        return wrapper


@BigContainer('plain cardboard')
@WarehouseDecorator('bubble foil')
def pack_books(*args):
    print("We'll pack books:", args)


@BigContainer('colourful cardboard')
@WarehouseDecorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)


@BigContainer('strong cardboard')
@WarehouseDecorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)


pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')
