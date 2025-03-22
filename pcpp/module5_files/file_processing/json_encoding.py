import json


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model


def encode_car(car):
    if isinstance(car, Car):
        return car.__dict__
    else:
        raise TypeError(f'{car.__class__.__name__} is not serializable.')


def decode_car(flat_car):
    # return Car(flat_car['make'], flat_car['model'])
    return Car(**flat_car)


class CarEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Car):
            return o.__dict__
        else:
            raise TypeError(f'{o.__class__.__name__} is not serializable.')


class CarDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_car)

    def decode_car(self, flat_car):
        return Car(**flat_car)


obj_car = Car("Maruti Suzuki", "Swift")
car_json = json.dumps(obj_car, default=encode_car)
print(car_json)
car_json = json.dumps(obj_car, cls=CarEncoder)
print(car_json)
obj_car = json.loads(car_json, object_hook=decode_car)
print(obj_car)
obj_car = json.loads(car_json, cls=CarDecoder)
print(obj_car)

