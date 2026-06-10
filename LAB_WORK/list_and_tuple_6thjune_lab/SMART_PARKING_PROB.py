# List representing parking slots
# 1 = Occupied, 0 = Available
slots = [1, 0, 1, 1, 0, 0, 1, 0]

# Count occupied and available slots
occupied = 0
available = 0

for slot in slots:
    if slot == 1:
        occupied += 1
    else:
        available += 1

print("Occupied Slots:", occupied)
print("Available Slots:", available)


# Find the first available slot
for i in range(len(slots)):
    if slots[i] == 0:
        print("First Available Slot:", i + 1)
        break


# Display all available slot numbers
print("Available Slot Numbers:")

for i in range(len(slots)):
    if slots[i] == 0:
        print(i + 1, end=" ")

print()


# Check if occupancy exceeds 75%
occupancy = (occupied / len(slots)) * 100

print("Occupancy Percentage:", occupancy, "%")

if occupancy > 75:
    print("Parking occupancy exceeds 75%")
else:
    print("Parking occupancy does not exceed 75%")