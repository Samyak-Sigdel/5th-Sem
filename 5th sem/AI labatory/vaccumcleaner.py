def vaccumm(location, status):
    global flag
    global locations_status

    if status == "Dirty":
        flag += 1
        locations_status[location] = "Already Cleaned"
        return 'Sucking the dirt in location'
    else:
        locations_status[location] = "Already Cleaned"
        return 'Already cleaned location'

flag = 0
locations_status = {}  

n = int(input("Enter number of locations: ")) 

for x in range(n):
    location = input(f"Location {x+1}: ")
    status = input("Status (Dirty/Clean): ")
    action = vaccumm(location, status)
    print(f"{location}: {action} {location}")

print(f"Total dirty locations cleaned: {flag}")

print("\nLocation Status Check:")
for location in locations_status:
    status = locations_status[location]
    print(f"{location}: {status}")