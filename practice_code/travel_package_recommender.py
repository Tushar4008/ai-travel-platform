traveler_name = input("Enter your name: ")
traveler_age = int(input("Enter your age: "))
budget = int(input("Enter your budget in rupees: "))
passport_available = input("Do you have a passport?(yes/no)").strip().lower() == 'yes'
booking_status = ""
recommended_package = ""

if traveler_age<18:
    print("Booking not allowed")
    booking_status = "Booking declined"
    recommended_package = "N/A"

elif not passport_available:
    print("Domestic Packages only")
    booking_status = "Domestic booking accepted"
    recommended_package = "Domestic"

else:
    booking_status = "Booking accepted"
    if budget >= 100000:
        recommended_package = 'Luxury'

    elif budget >= 50000:
        recommended_package = "Premium"

    elif budget >= 20000:
        recommended_package = "Standard"

    else:
        recommended_package = "Budget"

print("Traveler Summary")
print("--"*8)
print(f"Traveler name- {traveler_name}")
print(f"Traveler age- {traveler_age}")
print(f"Traveler budget- {budget}")
print(f"Passport Available: {'Yes' if passport_available else 'No'}")
print(f"Recommended package- {recommended_package}")    
print(f"Booking status- {booking_status}")