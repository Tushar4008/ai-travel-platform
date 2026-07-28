prices = {
    "Thailand":55000,
    "Japan":90000,
    "Dubai":40000
}

user_destination = input("Enter your destination: ").strip().title()

if user_destination in prices:
    print(prices[user_destination])
else:
    print("Package not available")