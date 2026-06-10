def display():
    f = open("expenses.txt", "r")
    print(f.read())
    f.close()


def total():
    f = open("expenses.txt", "r")
    s = 0

    for line in f:
        amt = int(line.strip().split(",")[1])
        s += amt

    print("Total Expenses = ₹", s)
    f.close()


def high_low():
    f = open("expenses.txt", "r")

    first = f.readline()
    cat, amt = first.strip().split(",")

    high_cat = low_cat = cat
    high = low = int(amt)

    for line in f:
        cat, amt = line.strip().split(",")
        amt = int(amt)

        if amt > high:
            high = amt
            high_cat = cat

        if amt < low:
            low = amt
            low_cat = cat

    print("Highest:", high_cat, "₹", high)
    print("Lowest:", low_cat, "₹", low)

    f.close()


def above_800():
    f = open("expenses.txt", "r")

    print("Expenses above ₹800:")
    for line in f:
        cat, amt = line.strip().split(",")

        if int(amt) > 800:
            print(cat, amt)

    f.close()


def add():
    cat = input("Enter category: ")
    amt = input("Enter amount: ")

    f = open("expenses.txt", "a")
    f.write(f"\n{cat},{amt}")
    f.close()

    print("Expense added")


def update():
    category = input("Enter category to update: ")

    f = open("expenses.txt", "r")
    data = f.readlines()
    f.close()

    f = open("expenses.txt", "w")

    for line in data:
        cat, amt = line.strip().split(",")

        if cat.lower() == category.lower():
            amt = input("Enter new amount: ")
            print("Expense updated")

        f.write(f"{cat},{amt}\n")

    f.close()


def report():
    f = open("expenses.txt", "r")
    data = f.readlines()
    f.close()

    total = 0
    high = -1
    low = 999999
    high_cat = low_cat = ""

    r = open("report.txt", "w")

    r.write("SUMMARY REPORT\n")

    for line in data:
        cat, amt = line.strip().split(",")
        amt = int(amt)

        total += amt

        if amt > high:
            high = amt
            high_cat = cat

        if amt < low:
            low = amt
            low_cat = cat

    r.write(f"Total Expenses: ₹{total}\n")
    r.write(f"Highest Expense: {high_cat} ₹{high}\n")
    r.write(f"Lowest Expense: {low_cat} ₹{low}\n")

    r.write("Expenses above ₹800:\n")

    for line in data:
        cat, amt = line.strip().split(",")

        if int(amt) > 800:
            r.write(f"{cat} ₹{amt}\n")

    r.close()

    print("Report generated in report.txt")


# Main Program
while True:
    print("\n1. Display Expenses")
    print("2. Total Expenditure")
    print("3. Highest & Lowest Spending")
    print("4. Expenses > ₹800")
    print("5. Add Expense")
    print("6. Update Expense")
    print("7. Generate Report")
    print("8. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        display()

    elif ch == 2:
        total()

    elif ch == 3:
        high_low()

    elif ch == 4:
        above_800()

    elif ch == 5:
        add()

    elif ch == 6:
        update()

    elif ch == 7:
        report()

    elif ch == 8:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")