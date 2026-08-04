def welcome():
    print("Welcome Traveler")

def calculate_price(price:int, discount:int)->int:
    total_price=price-discount
    return total_price

def trip_duration(days:int):
    return f"Total number of travel days are {days}"

def save_destination(destination:str):
    with open("/Users/tusharshukla/Documents/WanderlustWingss/docs/destinations.txt","a") as file:
        file.write(f"\n{destination}")

def load_destinations():
    countries=set()
    with open("/Users/tusharshukla/Documents/WanderlustWingss/docs/destinations.txt") as file:
        for line in file:
            countries.add(line.strip())
    return countries