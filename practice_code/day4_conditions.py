traveler_name = input("Enter your name: ")
budget = int(input("Enter your budget: "))
passport_available = input("Do you have a passport?(yes/no)").strip().lower() == 'yes'

print()

if passport_available and budget >= 30000:
    print("International package available")
else:
    print("Domestic package recommended")
