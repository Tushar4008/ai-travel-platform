class TravelPackage:

    def __init__(self,destination,price,discount,days):
        self.destination= destination
        self.price= price
        self.discount= discount
        self.days= days
        
    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self,destination):

        if destination == "":
            raise ValueError("Destination can't be empty")
        self._destination=destination

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):

        if price<=0:
            raise ValueError("Price can't be less than zero")
        self._price=price        

    @property
    def days(self):
        return self._days
    
    @days.setter
    def days(self, days):
    
        if days<=0:
            raise ValueError("Days can't be less than zero")
        self._days= days

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        if discount < 0:
            raise ValueError("Discount can't be negative")
        self._discount = discount

    @property
    def final_price(self):
        if self.discount>=0:
            return self.price-self.discount

package1= TravelPackage("Thailand",1000,100,10)
print(f"{package1.destination}, {package1.price}, {package1.days}, {package1.final_price}")


class Booking:

    def __init__(self,traveler_name,destination,price): 
        self.traveler_name=traveler_name
        self.destination=destination
        self.price= price

    @property
    def booking_summary(self):        
        return f"{self.traveler_name} booked {self.destination} for ₹{self.price}"

booking1=Booking("Tushar","Thailand",10000)
print(booking1.booking_summary)