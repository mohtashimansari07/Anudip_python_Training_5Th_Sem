# Passenger records
passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]

confirmed = []
waiting = []

# Display waiting-list passengers and create separate lists
print("Waiting-list passengers:")
for name, status in passengers:
    if status == "Waiting":
        print(name)
        waiting.append(name)
    else:
        confirmed.append(name)

# Count confirmed and waiting passengers
print("\nConfirmed passengers:", len(confirmed))
print("Waiting passengers:", len(waiting))

# Check if a specific passenger has a confirmed ticket
search = input("\nEnter passenger name: ")

found = False
for name, status in passengers:
    if name.lower() == search.lower():
        found = True
        if status == "Confirmed":
            print(name, "has a confirmed ticket.")
        else:
            print(name, "does not have a confirmed ticket.")
        break

if not found:
    print("Passenger not found.")

# Display separate lists
print("\nConfirmed List:", confirmed)
print("Waiting List:", waiting)