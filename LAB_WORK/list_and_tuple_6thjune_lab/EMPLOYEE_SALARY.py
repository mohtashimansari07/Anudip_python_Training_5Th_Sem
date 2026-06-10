# List of employee data (Name, Salary)
employees = [
    ("Rahul", 35000),
    ("Priya", 55000),
    ("Amit", 42000),
    ("Neha", 65000)
]

# Display employees earning above ₹50,000
print("Employees earning above ₹50,000:")
for emp in employees:
    if emp[1] > 50000:
        print(emp[0], "-", emp[1])

# Find the highest-paid employee
highest = employees[0]

for emp in employees:
    if emp[1] > highest[1]:
        highest = emp

print("\nHighest-paid employee:")
print(highest[0], "-", highest[1])

# Calculate total salary expenditure
total = 0

for emp in employees:
    total += emp[1]

print("\nTotal Salary Expenditure: ₹", total)

# Count employees earning below ₹40,000
count = 0

for emp in employees:
    if emp[1] < 40000:
        count += 1

print("\nEmployees earning below ₹40,000:", count)