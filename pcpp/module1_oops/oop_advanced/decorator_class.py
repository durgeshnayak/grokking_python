class SimpleDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        print(f'{self.function.__name__} was called with following positional arguments: {args}')
        print(f'{self.function.__name__} was called with following keyword arguments: {kwargs}')
        print('Calling function now.........')
        self.function(*args, **kwargs)
        print('Decorator signing off........')


@SimpleDecorator
def combiner(*args, **kwargs):
    print(f'Hello from combiner function; received positional arguments: {args} & keyword arguments: {kwargs}')


combiner('durgesh', 'agile coach', org="IBM", country="India")

