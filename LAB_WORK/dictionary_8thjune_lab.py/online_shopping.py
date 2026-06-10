# Product sales data
sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

# 1. Display products sold more than 20 times
print("Products Sold More Than 20 Times:")
for product in sales:
    if sales[product] > 20:
        print(product)

# 2. Find the best-selling product
best = max(sales, key=sales.get)

# 3. Find the least-selling product
least = min(sales, key=sales.get)

# 4. Calculate total products sold
total = 0
for product in sales:
    total += sales[product]

# 5. Create a list of products requiring promotion
promotion = []
for product in sales:
    if sales[product] < 15:
        promotion.append(product)

# 6. Count products having sales between 10 and 30
count = 0
for product in sales:
    if 10 <= sales[product] <= 30:
        count += 1

# Display results
print("\nBest Selling Product:", best, "(", sales[best], ")", sep="")
print("Least Selling Product:", least, "(", sales[least], ")", sep="")
print("Total Units Sold:", total)

print("\nProducts Requiring Promotion:")
print(promotion)

print("\nProducts Having Sales Between 10 and 30:", count)