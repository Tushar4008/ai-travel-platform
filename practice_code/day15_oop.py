class Traveler:
    def __init__(self,name,age,country,passport_available):
        self.name=name
        self.age=age
        self.country=country
        self.passport_available=passport_available

    def display_profile(self):
        print(f"Traveler: {self.name}")
        print(f"Age: {self.age}")
        print(f"Country: {self.country}")
        print(f"Passport Available: {self.passport_available}")

    def check_international_eligibility(self):
        if self.age>=18 and self.passport_available:
            print(f"{self.name} Eligible for International Travel")
        else:
            print(f"{self.name} Not Eligible for International Travel") 

traveler1 = Traveler("Tushar",18,"India",True)
traveler2 = Traveler("Shaurya",28,"USA",False)

traveler1.display_profile()
traveler2.display_profile()

traveler1.check_international_eligibility()
traveler2.check_international_eligibility()
