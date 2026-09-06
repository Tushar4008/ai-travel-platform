class Traveler:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):

        if value < 0:
            raise ValueError("Age cannot be negative")

        self._age = value


traveler = Traveler("Tushar", 30)

print(traveler.age)

traveler.age = -2

print(traveler.age)