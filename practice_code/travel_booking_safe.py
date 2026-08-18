try:
    budget = int(input("Enter the budget"))
except ValueError:
    print("Invalid Budget Value")
else:
    print(f"Buget is {budget}")
finally:
    print("Thank you for using Wanderlust Wings")

try:
    traveler_count = int(input("Enter the number of Travelers"))
    if traveler_count<=0:
        raise ValueError
except ValueError:
    print("The number of traveler are invalid")
else:
    print(f"Number of travelers are {traveler_count}")
finally:
    print("Thank you for using Wanderlust Wings")

try: 
    with open("/Users/tusharshukla/Documents/WanderlustWingss/docs/booking_history1.txt") as file: 
        print(file.read())
except FileNotFoundError:
    print("Booking history unavailable.")
finally:
    print("Thank you for using Wanderlust Wings")


    