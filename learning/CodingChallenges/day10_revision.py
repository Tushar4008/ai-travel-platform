destinations = [
    "Goa",
    "Thailand",
    "Goa",
    "Japan",
    "Thailand",
    "Dubai",
    "Goa"
]

destination_set = set()
duplicate_set = set()

for destination in destinations:
    if destination in destination_set:
        duplicate_set.add(destination)
    else:
        destination_set.add(destination)

print(duplicate_set)

# def find_duplicate_destinations(destinations):
#     final_list=set()
#     for i in range(0,len(destinations)-1):
#         count=0
#         for j in range(i+1,len(destinations)):
#             if destinations[i]==destinations[j]:
#                 count+=1
#         if count>0: 
#             final_list.add(destinations[i])
#     return final_list

# print(find_duplicate_destinations(destinations))

