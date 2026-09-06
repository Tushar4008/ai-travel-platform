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

    def check_international_eligibility(self):
        if self.age>=18 and self.passport_available==True:
            return f"{self.name} is eligible for international travel"
        else:
            return f"{self.name} is not eligible for international travel"

    @property
    def profile_summary(self):
        return f"{self.name} | {self.age} | {self.country} | Passport: {self.passport_available}"

traveler1=Traveler("Tushar",30,"India",True)
traveler2=Traveler("Shaurya",27,"India",False)
traveler3=Traveler("Kid",17,"India",True)

print(traveler1.check_international_eligibility())
print(traveler2.check_international_eligibility())
print(traveler3.check_international_eligibility())
