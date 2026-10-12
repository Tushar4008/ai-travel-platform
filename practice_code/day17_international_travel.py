class Traveler:
    def __init__(self,name ,age, country):
        self.name = name
        self.age = age
        self.country = country

    def display_profile(self):
        return f"Name: {self.name}, Age: {self.age}, Country: {self.country}"

class InternationalTraveler(Traveler):
    def __init__(self, name, age, country, passport_available):
        super().__init__(name, age, country)
        self.passport_available = passport_available

    def check_international_eligibility(self):
        if self.age >= 18 and self.passport_available:
            return f"Eligible"
        else:
            return "Not Eligible"

traveler1= InternationalTraveler("Tushar",30,"India",False)

print(traveler1.check_international_eligibility())