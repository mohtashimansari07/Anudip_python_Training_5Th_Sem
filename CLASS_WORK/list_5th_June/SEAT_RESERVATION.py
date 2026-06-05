# Bus seats (1 = booked, 0 = available)
seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

booked = 0
available = []
first_seat = 0

# Check each seat
for i in range(len(seats)):

    if seats[i] == 1:
        booked += 1
    else:
        available.append(i + 1)  # Store seat number

        # Find first available seat
        if first_seat == 0:
            first_seat = i + 1

# Calculate occupancy
occupancy = (booked / len(seats)) * 100

# Print results
print("Booked Seats:", booked)
print("Available Seats:", len(available))
print("First Available Seat:", first_seat)
print("Available Seat Numbers:", available)
print("Bus Occupancy:", occupancy, "%")

# Check occupancy status
if occupancy > 70:
    print("Status: More Than 70% Occupied")
else:
    print("Status: Not More Than 70% Occupied")