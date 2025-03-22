import random


class Apple:

    def __init__(self):
        self.weight = random.uniform(a=0.2, b=0.5)


class Packer:

    def __init__(self):
        self.apple_count = 0
        self.weight = 0
        self.pack = True


    def add_apple(self, new_apple: Apple):
        if self.check_weight(new_apple):
            self.apple_count += 1
            self.weight += new_apple.weight
        else:
            self.pack = False
            print("Basket full, packaging process has been stopped.")
            print(f"Total number of apples added: {self.apple_count} and weight of basket is {round(self.weight)}")

    def check_weight(self, new_apple: Apple):
        if self.weight + new_apple.weight <= 300:
            return True
        else:
            return False


packer = Packer()
while packer.pack:
    apple = Apple()
    packer.add_apple(new_apple=apple)


