class TravelPackage:
    def __init__(self,destination,price):
        self.destination = destination
        self.price = price

    def display_profile(self):
        print( f"Destination: {self.destination},Price: {self.price}")

    def calculate_price(self):
        return self.price

class PremiumPackage(TravelPackage):
    def __init__(self, destination, price, premium_service):
        super().__init__(destination, price)
        self.premium_service = premium_service

    def display_profile(self):
        super().display_profile()
        print (f"Premium Service: {self.premium_service}")

package1= PremiumPackage("Thailand",1000001,True)
(package1.display_profile())

class Luxury_Package(TravelPackage):
    def __init__(self, destination, price, luxury_fees):
        super().__init__(destination, price)
        self.luxury_fees = luxury_fees

    def calculate_price(self):
        return self.price+self.luxury_fees

package2 = Luxury_Package("Dubai",200000,5000)
print(f"Total price for {package2.destination} is {package2.calculate_price()}")