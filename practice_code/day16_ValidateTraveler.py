class Traveler:
    def __init__(self,name,age,country,passport_available):
        self.name = name
        if age<0:
            raise ValueError("Age can't be in negative")
        self.age=age
        if country == "":
            raise ValueError("Country can't be empty")
        self.country=country
        if passport_available not in [True,False]:
            raise ValueError("Passport availability should be True/False")
        self.passport_available=passport_available


traveler1=Traveler("Tushar",30,"I",True)
print(f"{traveler1.name}, {traveler1.age}, {traveler1.country}, {traveler1.passport_available}")