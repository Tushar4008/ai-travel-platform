# Problem

# You are given a list of destinations.

# destinations = [
#     "Goa",
#     "Thailand",
#     "Goa",
#     "Japan",
#     "Japan",
#     "Dubai"
# ]

# Return a new list that contains only the first occurrence of each destination while preserving the original order.

# Expected output:

# [
#     "Goa",
#     "Thailand",
#     "Japan",
#     "Dubai"
# ]
# Constraints

# ❌ Do NOT use:

# list(set(destinations))

# because that doesn't preserve order.

# destinations = [
#     "Goa",
#     "Thailand",
#     "Goa",
#     "Japan",
#     "Japan",
#     "Dubai"
# ]

# def return_unique():
#     for i in range(0,len(destinations)):
#         for j in range(i+1,len(destinations)-1):
#             if destinations[i]==destinations[j]:
#                 destinations.pop(j)

#     return destinations

# print(return_unique())


destinations = [
    "Goa",
    "Thailand",
    "Goa",
    "Japan",
    "Japan",
    "Dubai"
]

seen = set()
result= []

def unique_return():
    for destination in destinations:
        if destination not in seen:
            seen.add(destination)
            result.append(destination)
    return result

print(unique_return())