# Employee performance scores
performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

# 1. Display employees scoring above 80
print("Employees Scoring Above 80:")
for emp, score in performance.items():
    if score > 80:
        print(emp)

# 2. Count employees needing improvement
improvement_count = 0

# Lists for categories
excellent = []
good = []
average = []
poor = []

total = 0

for emp, score in performance.items():
    total += score

    if score < 60:
        improvement_count += 1
        poor.append(emp)
    elif score >= 90:
        excellent.append(emp)
    elif 75 <= score <= 89:
        good.append(emp)
    elif 60 <= score <= 74:
        average.append(emp)

# 3. Find the top performer
top_emp = max(performance, key=performance.get)

# 4. Calculate average performance score
avg_score = total / len(performance)

# Display results
print("\nTop Performer:", top_emp, "(", performance[top_emp], ")", sep="")

print("\nEmployees Needing Improvement:", improvement_count)

print("\nAverage Score:", round(avg_score, 1))

print("\nExcellent:")
print(excellent)

print("\nGood:")
print(good)

print("\nAverage:")
print(average)

print("\nPoor:")
print(poor)