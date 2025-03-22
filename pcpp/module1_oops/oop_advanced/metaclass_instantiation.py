import datetime


def get_instantiation_time(self):
    return self.__class__.instantiation_time


class InstantiationMetaclass(type):
    Instantiated_Classes = []
    instantiation_time = None

    def __new__(mcs, name, bases, dictionary):
        dictionary['get_instantiation_time'] = get_instantiation_time
        obj = super().__new__(mcs, name, bases, dictionary)
        obj.instantiation_time = datetime.datetime.now().strftime('%Y-%M-%d %H:%m:%S.%f')
        InstantiationMetaclass.Instantiated_Classes.append(name)
        return obj


class Hobbit(metaclass=InstantiationMetaclass):
    pass


class Dwarf(metaclass=InstantiationMetaclass):
    pass


frodo = Hobbit()
bombur = Dwarf()

print(Hobbit.Instantiated_Classes)
print(frodo.get_instantiation_time())
print(Dwarf.Instantiated_Classes)
print(bombur.get_instantiation_time())
