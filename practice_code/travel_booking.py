def welcome():
    print("Welcome to Wanderlust Wings!")

welcome()

def greet_user(name):
    print(f"Welcome {name}!")

greet_user("Shaurya")

def calculate_price(price, discount):
    return price-discount

final_price=calculate_price(50000,2500)
print(final_price)

def package_details(destination, days):
    return f"{destination} package for {days} days"

print(package_details("Thailand",15))


