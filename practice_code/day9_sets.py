destinations = {
    "Thailand",
    "Japan",
    "Thailand",
    "Dubai"
}

visited_destinations = {
    "Vietnam",
    "Thailand",
    "India"
}

destinations.add("India")

print(destinations)

destinations.discard("Dubai")

if "Thailand" in destinations:
    print("Available")

for country in destinations:
    print(country)

print(destinations | visited_destinations)

print(destinations - visited_destinations)

print(destinations & visited_destinations)

print(destinations ^ visited_destinations)