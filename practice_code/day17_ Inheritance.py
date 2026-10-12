class Traveler:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_profile(self):
        return f"The name of traveler is {self.name} and age is {self.age}"

    def travel_message(self):
        return f"Name: {self.name}, Age: {self.age}"


class InternationalTraveler(Traveler):

    def __init__(self,name,age,passport_number):
        super().__init__(name, age)
        self.passport_number = passport_number

    def check_passport(self):
        return f"The passport number is {self.passport_number}"

    def travel_message(self):
        return f"Name: {self.name}, Age: {self.age}, Passport Number: {self.passport_number}"

    def display_profile(self):
        print(super().display_profile())
        print(f"Passport Number: {self.passport_number}")


traveler1 = InternationalTraveler("Tushar",30,"KGV")

traveler1.display_profile()
print(traveler1.check_passport())

print(traveler1.travel_message())