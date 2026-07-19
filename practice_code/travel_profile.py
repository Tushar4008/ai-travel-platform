traveler_name = input("Enter your name: ")
traveler_age = int(input("Enter your age: "))
traveler_country = input("Enter your home country: ")
favorite_Destination = input("Enter your favorite destination: ")
budget = int(input("Enter your budget in rupees: "))
passport_available = input("Do you have a passport(yes or no)?: ")

traveler_name=traveler_name.strip()
traveler_country=traveler_country.strip()
favorite_Destination =favorite_Destination.strip()
passport_available = passport_available.strip()

traveler_name = traveler_name.title()
favorite_Destination = favorite_Destination.title()

passport_available = passport_available.strip().lower() == 'yes'

print("\nTraveler Profile- ")
print(f"Traveler name- {traveler_name}")
print(f"Traveler age- {traveler_age}")
print(f"Traveler country- {traveler_country}")
print(f"Destination- {favorite_Destination}")
print(f"Travler budget- {budget}")
print(f"Is passport available- {passport_available}")

print(len(traveler_name))
print(favorite_Destination[0])
print(favorite_Destination[-1])
print(favorite_Destination.startswith('T'))
print(favorite_Destination.endswith('land'))



