flight = (
    "AI302",
    "Delhi",
    "Bangkok",
    25000
)

print(f"Fight Number- {flight[0]}")

print(f"Source- {flight[1]}")

print(f"Destination- {flight[2]}")

print(f"Ticket Price- {flight[3]}")

flight_number,source_city,destination_city,ticket_price = flight

print(flight_number,source_city,destination_city,ticket_price)

for item in flight:
    print(item)

print(f"Number of items in flight- {len(flight)}")