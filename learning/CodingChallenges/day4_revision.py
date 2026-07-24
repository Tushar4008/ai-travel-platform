cities = (
    "Delhi",
    "Goa",
    "Mumbai"
)

favourite_city= input("Enter your favourite city: ")

if favourite_city in cities:
    print("Available")
else:
    print("Not Available")