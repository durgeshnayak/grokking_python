class TankError(Exception):
    pass


class Tank:
    def __init__(self, capacity):
        self.capacity = capacity
        self.__level = 0

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, amount):
        if amount > 0:
            if amount <= self.capacity:
                self.__level = amount
            else:
                raise TankError("Too much liquid in the tank.")
        else:
            raise TankError("Not possible to set negative value for level.")

    @level.deleter
    def level(self):
        if self.__level > 0:
            print("It is good to remember to sanitize the remains from the tank!")
        self.__level = None


# our tank object has a capacity of 20 units
our_tank = Tank(capacity=20)
print(f"Current liquid level: {our_tank.level}")

# our tank's current level is set to 10 units
our_tank.level = 10
print(f"Current liquid level: {our_tank.level}")

# adding additional 3 units (making level to 13 units)
our_tank.level += 3
print(f"Current liquid level: {our_tank.level}")

# let's try to set the liquid level to 21 units
try:
    our_tank.level = 21
except TankError as e:
    print(f"Trying to set the liquid level to 21, result: {e}")

# let's try to add another 15 units
try:
    our_tank.level += 15
except TankError as e:
    print(f"Tried adding 15 units, result: {e}")

# let's try setting the level to a negative value
try:
    our_tank.level = -3
except TankError as e:
    print(f"Trying to set the liquid level to -3, result: {e}")

del our_tank.level