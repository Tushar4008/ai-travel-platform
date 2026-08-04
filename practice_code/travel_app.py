import travel_utils

travel_utils.welcome()

final_price= travel_utils.calculate_price(50000,2500)
print(f"The total cost of package is {final_price}")

print(travel_utils.trip_duration(5))

travel_utils.save_destination("Thailand")

travel_utils.save_destination("Japan")

unique_countries= travel_utils.load_destinations()
print(unique_countries)
