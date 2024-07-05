total_locations = int(input("Enter the total number of locations: "))
places = []

for _ in range(total_locations):
    location = input("Enter the location: ")
    status = input("Enter the location status : ")
    places.append((location, status))



def vacuum(status):
    if status == "Dirty":
        return "Suck the dirt in location "
    else:
        return "The place is cleaned"

for location, status in places:
    result = vacuum(status)
    print(f" {result} {location}")

def suck():
    return "Sucking dirt"

for location, status in places:
    if status == "Dirty":
        result = suck()
        print(f" {result} {location}")
    else:
        print(f"The place is already clean {location}:")