available = {
    "Thailand",
    "Japan",
    "Dubai"
}

def check_destination(destination):
    if destination in available:
        return "Available"
    else:
        return "Not Available"
    
status=check_destination("Thailand")
print(status)