class TravelPackage:

    def __init__(self,destination,price,days):
        self.destination=destination
        self.price=price
        self.days=days

    def display_package(self):
        print(f"Destination: {self.destination}")
        print(f"Price: {self.price}")
        print(f"Days: {self.days}")

    def calculate_discount(self,discount):
        final_price=self.price-discount
        return final_price

    def is_luxury(self):
        if self.price>=100000:
            return True
        else:
            return False


package1= TravelPackage("Japan",200000,10)
package2= TravelPackage("Thailand",150000,15)
package3= TravelPackage("India",20000,7)

package1.display_package()

print(f"Final Price for {package2.destination}: {package2.calculate_discount(5000)}")

print(f"Is {package3.destination} a luxury package? {package3.is_luxury()}")