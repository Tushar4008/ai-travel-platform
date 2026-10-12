packages = [
    {"destination": "Thailand", "price": 55000},
    {"destination": "Japan", "price": 120000},
    {"destination": "Dubai", "price": 80000},
    {"destination": "Japan", "price": 120000}
]

def package_analyzer(packages):
    unique_destinations = set()
    luxury_list = []
    for d in packages:
        unique_destinations.add(d["destination"])
        if d["price"]>=100000:
            luxury_list.append(d["destination"])

    t = unique_destinations,luxury_list,len(unique_destinations)
    return t

print(package_analyzer(packages))
    