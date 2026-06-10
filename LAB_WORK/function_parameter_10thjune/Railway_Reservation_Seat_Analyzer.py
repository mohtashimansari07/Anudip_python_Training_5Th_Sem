#using function parameters Railway Reservation Seat Analyzer
"""Problem Statement 
A railway coach has seats represented as follows: 
seats = [ 
    "Booked", "Available", "Booked", "Booked", 
    "Available", "Available", "Booked", "Available", 
    "Booked", "Booked", "Available", "Booked" 
] 
Requirements 
Create the following functions: 
1. count_seats(seats) 
Returns the number of booked and available seats. 
2. first_available(seats) 
Returns the seat number of the first available seat. 
3. occupancy_percentage(seats) 
Returns the percentage of occupied seats. 
4. display_available_seats(seats) 
Displays all available seat numbers."""

# List of seats
seats = [
    "Booked", "Available", "Booked", "Booked",
    "Available", "Available", "Booked", "Available",
    "Booked", "Booked", "Available", "Booked"
]

# 1. Count booked and available seats
def count_seats(seats):     # seats is a parameter
    booked = 0
    available = 0

    for seat in seats:
        if seat == "Booked":
            booked += 1
        else:
            available += 1

    print("Booked Seats:", booked)
    print("Available Seats:", available)


# 2. Find first available seat
def first_available(seats):     # seats is a parameter
    for i in range(len(seats)):
        if seats[i] == "Available":
            print("First Available Seat:", i + 1)
            return

    print("No seats available")


# 3. Calculate occupancy percentage
def occupancy_percentage(seats):     # seats is a parameter
    booked = 0

    for seat in seats:
        if seat == "Booked":
            booked += 1

    percentage = (booked / len(seats)) * 100
    print("Occupancy Percentage:", percentage, "%")


# 4. Display available seat numbers
def display_available_seats(seats):     # seats is a parameter
    print("Available Seat Numbers:")

    for i in range(len(seats)):
        if seats[i] == "Available":
            print(i + 1, end=" ")

    print()


# Function calls (seats is passed as an argument)
count_seats(seats)
first_available(seats)
occupancy_percentage(seats)
display_available_seats(seats)