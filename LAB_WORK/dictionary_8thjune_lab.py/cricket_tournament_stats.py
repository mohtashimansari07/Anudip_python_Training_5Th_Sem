# Runs scored by players
runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

# 1. Display players scoring more than 500 runs
print("Players Scoring More Than 500 Runs:")
for player in runs:
    if runs[player] > 500:
        print(player)

# 2. Find the Orange Cap winner
orange_cap = max(runs, key=runs.get)

# 3. Find the lowest scorer
lowest = min(runs, key=runs.get)

# 4. Calculate total runs scored
total_runs = 0
for player in runs:
    total_runs += runs[player]

# 5. Create a list of players scoring below 400
below_400 = []
for player in runs:
    if runs[player] < 400:
        below_400.append(player)

# 6. Count players scoring between 400 and 600 runs
count = 0
for player in runs:
    if 400 <= runs[player] <= 600:
        count += 1

# Display results
print("\nOrange Cap Winner:", orange_cap, "(", runs[orange_cap], ")", sep="")
print("Lowest Scorer:", lowest, "(", runs[lowest], ")", sep="")
print("Total Tournament Runs:", total_runs)

print("\nPlayers Scoring Below 400:")
print(below_400)

print("\nPlayers Between 400 and 600 Runs:", count)