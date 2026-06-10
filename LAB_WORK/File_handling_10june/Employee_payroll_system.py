

while True:
    print("\n----- EMPLOYEE MANAGEMENT SYSTEM -----")
    print("1. Display all employee records")
    print("2. Search employee by ID")
    print("3. Calculate average salary")
    print("4. Find highest-paid and lowest-paid employee")
    print("5. Display employees earning above ₹50,000")
    print("6. Add a new employee record")
    print("7. Generate salary categories")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Display all records
    if choice == 1:
        f = open("employees.txt", "r")
        print("\nEmployee Records:")
        for line in f:
            print(line.strip())
        f.close()

    # 2. Search employee by ID
    elif choice == 2:
        emp_id = input("Enter Employee ID: ")
        found = False

        f = open("employees.txt", "r")
        for line in f:
            eid, name, salary = line.strip().split(",")

            if eid == emp_id:
                print("\nEmployee Found")
                print("ID:", eid)
                print("Name:", name)
                print("Salary:", salary)
                found = True
                break

        f.close()

        if not found:
            print("Employee not found.")

    # 3. Calculate average salary
    elif choice == 3:
        total = 0
        count = 0

        f = open("employees.txt", "r")
        for line in f:
            eid, name, salary = line.strip().split(",")
            total += int(salary)
            count += 1

        f.close()

        average = total / count
        print("Average Salary = ₹", average)

    # 4. Highest-paid and lowest-paid employee
    elif choice == 4:
        f = open("employees.txt", "r")

        first = f.readline()
        eid, name, salary = first.strip().split(",")

        max_name = min_name = name
        max_salary = min_salary = int(salary)

        for line in f:
            eid, name, salary = line.strip().split(",")
            salary = int(salary)

            if salary > max_salary:
                max_salary = salary
                max_name = name

            if salary < min_salary:
                min_salary = salary
                min_name = name

        f.close()

        print("Highest Paid:", max_name, "- ₹", max_salary)
        print("Lowest Paid:", min_name, "- ₹", min_salary)

    # 5. Employees earning above 50000
    elif choice == 5:
        print("\nEmployees earning above ₹50,000:")

        f = open("employees.txt", "r")
        for line in f:
            eid, name, salary = line.strip().split(",")

            if int(salary) > 50000:
                print(eid, name, salary)

        f.close()

    # 6. Add new employee record
    elif choice == 6:
        eid = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        salary = input("Enter Salary: ")

        f = open("employees.txt", "a")
        f.write("\n" + eid + "," + name + "," + salary)
        f.close()

        print("Employee record added successfully.")

    # 7. Salary categories
    elif choice == 7:
        print("\nSalary Categories:")

        f = open("employees.txt", "r")
        for line in f:
            eid, name, salary = line.strip().split(",")
            salary = int(salary)

            if salary >= 60000:
                category = "High"
            elif salary >= 40000:
                category = "Medium"
            else:
                category = "Low"

            print(eid, name, "₹" + str(salary), "-", category)

        f.close()

    # 8. Exit
    elif choice == 8:
        print("Exiting program...")
        break

    else:
        print("Invalid choice.")