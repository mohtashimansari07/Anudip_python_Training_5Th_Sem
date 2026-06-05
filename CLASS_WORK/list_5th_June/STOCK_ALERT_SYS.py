# Stock quantities
stock = [25, 5, 0, 12, 3, 18, 0, 30]

# Empty variables and lists
out_stock = 0
available = 0
restock = []
healthy = []

# Check each stock value
for s in stock:

    # Count out of stock products
    if s == 0:
        out_stock += 1

    # Add products needing restock
    if s < 10:
        restock.append(s)

    # Count available products
    if s > 0:
        available += 1

    # Add healthy stock products
    if s >= 15:
        healthy.append(s)

# Display results
print("Out of Stock Products:", out_stock)
print("Restock Required:", restock)
print("Available Products:", available)
print("Healthy Stock:", healthy)