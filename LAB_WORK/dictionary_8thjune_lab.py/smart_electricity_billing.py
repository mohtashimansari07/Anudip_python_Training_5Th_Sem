# Monthly electricity consumption (units)
units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

# 1. Display houses consuming more than 400 units
print("Houses Consuming More Than 400 Units:")
for house in units:
    if units[house] > 400:
        print(house)

# 2. Find the highest-consuming house
highest = max(units, key=units.get)

# 3. Find the lowest-consuming house
lowest = min(units, key=units.get)

# 4. Calculate total units consumed
total = 0
for house in units:
    total += units[house]

# 5. Create consumption lists
low = []
medium = []
high = []

for house in units:
    if units[house] < 200:
        low.append(house)
    elif 200 <= units[house] <= 400:
        medium.append(house)
    else:
        high.append(house)

# 6. Count houses eligible for energy-saving campaign
count = 0
for house in units:
    if units[house] > 300:
        count += 1

# Display results
print("\nHighest Consumption:")
print(highest, "(", units[highest], " units)", sep="")

print("\nLowest Consumption:")
print(lowest, "(", units[lowest], " units)", sep="")

print("\nTotal Units Consumed:", total)

print("\nLow Consumption:")
print(low)

print("\nMedium Consumption:")
print(medium)

print("\nHigh Consumption:")
print(high)

print("\nEligible for Energy-Saving Campaign:", count)