#using function parameters to build Food Delivery Performance Tracker
"""Problem Statement 
Delivery times (in minutes) for different orders are given below: 
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] 
Requirements 
Create the following functions: 
1. fastest_delivery(times) 
Returns the shortest delivery time. 
2. delayed_orders(times) 
Returns a list of orders taking more than 45 minutes. 
3. average_delivery_time(times) 
Returns the average delivery time. 
4. delivery_category(times) 
Displays order categories: 
• Fast → ≤ 30 minutes  
• Normal → 31-45 minutes  
• Delayed → > 45 minutes  """

# List of delivery times (in minutes)
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# Function to find the shortest delivery time
def fastest_delivery(times):
    fastest = times[0]      # Assume first delivery is the fastest

    for time in times:
        if time < fastest:
            fastest = time

    return fastest


# Function to return orders taking more than 45 minutes
def delayed_orders(times):
    delayed = []            # Empty list to store delayed orders

    for time in times:
        if time > 45:
            delayed.append(time)

    return delayed


# Function to calculate average delivery time
def average_delivery_time(times):
    total = 0               # Variable to store total delivery time

    for time in times:
        total += time

    average = total / len(times)

    return average


# Function to display delivery categories
def delivery_category(times):
    print("\nDelivery Categories:")

    for i in range(len(times)):

        # Categorize delivery based on time
        if times[i] <= 30:
            category = "Fast"
        elif times[i] <= 45:
            category = "Normal"
        else:
            category = "Delayed"

        # Display order number, time, and category
        print("Order", i + 1, ":", times[i], "minutes -", category)


# Calling the functions and displaying results
print("Fastest Delivery Time:",
      fastest_delivery(delivery_time), "minutes")

print("Delayed Orders:",
      delayed_orders(delivery_time))

print("Average Delivery Time:",
      average_delivery_time(delivery_time), "minutes")

delivery_category(delivery_time)