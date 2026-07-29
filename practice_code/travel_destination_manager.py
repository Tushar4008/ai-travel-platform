visited = {
    "Thailand",
    "Japan",
    "Dubai"
}

wishlist = {
    "Japan",
    "Singapore",
    "Bali"
}

print(f"Visited Countries: {visited}")

visited.add("Vietnam")

visited.discard("Dubai")

print(visited | wishlist)

print(visited & wishlist)

print(visited - wishlist)

print(visited ^ wishlist)

input_destination = input("Enter a destination: ").strip().title()

if input_destination in visited:
    print("Your destination is available")
else: 
    print("Your destination is not available")    