# Daily temperatures of different cities
temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

# 1. Display cities having temperature above 40°C
print("Cities Above 40°C:")
for city in temperature:
    if temperature[city] > 40:
        print(city)

# 2. Find the hottest city
hottest = max(temperature, key=temperature.get)

# 3. Find the coolest city
coolest = min(temperature, key=temperature.get)

# 4. Calculate average temperature
total = 0
for city in temperature:
    total += temperature[city]

average = total / len(temperature)

# 5. Create a list of pleasant cities
pleasant = []
for city in temperature:
    if temperature[city] < 35:
        pleasant.append(city)

# 6. Count cities with temperature between 35°C and 40°C
count = 0
for city in temperature:
    if 35 <= temperature[city] <= 40:
        count += 1

# Display results
print("\nHottest City:", hottest, "(", temperature[hottest], "°C)", sep="")
print("Coolest City:", coolest, "(", temperature[coolest], "°C)", sep="")
print("Average Temperature:", round(average, 1), "°C")

print("\nPleasant Cities:")
print(pleasant)

print("\nCities Between 35°C and 40°C:", count)