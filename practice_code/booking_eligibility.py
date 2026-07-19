traveler_name ='Tushar'
age = 30
budget = 15000
package_price = 10000
passport_available = True
available_seats = 5
destination = 'Goa'

can_book = (age>=18 and budget>=package_price and passport_available and available_seats>0)

print("Booking Summary")
print("---------------")
print(f"Traveler Name:{traveler_name}")
print(f"Destination:{destination}")
print(f"Budget:{budget}")
print(f"Package Price:{package_price}")
print(f"Can Book:{can_book}")
