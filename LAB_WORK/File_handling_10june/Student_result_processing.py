# Student Result Processing System
def display():
    f = open("students.txt", "r")
    print(f.read())
    f.close()


def search():
    sid = input("Enter Student ID: ")

    f = open("students.txt", "r")
    for line in f:
        if line.startswith(sid):
            print(line.strip())
            break
    else:
        print("Student not found")

    f.close()


def topper_lowest():
    f = open("students.txt", "r")

    first = f.readline()
    sid, name, marks = first.strip().split(",")

    top_name = low_name = name
    top_marks = low_marks = int(marks)

    for line in f:
        sid, name, marks = line.strip().split(",")
        marks = int(marks)

        if marks > top_marks:
            top_marks = marks
            top_name = name

        if marks < low_marks:
            low_marks = marks
            low_name = name

    print("Topper:", top_name, "-", top_marks)
    print("Lowest Scorer:", low_name, "-", low_marks)

    f.close()


def average():
    f = open("students.txt", "r")

    total = count = 0

    for line in f:
        marks = int(line.strip().split(",")[2])
        total += marks
        count += 1

    print("Class Average =", total / count)

    f.close()


def pass_fail():
    f = open("students.txt", "r")

    p = fail = 0

    for line in f:
        marks = int(line.strip().split(",")[2])

        if marks >= 40:
            p += 1
        else:
            fail += 1

    print("Pass:", p)
    print("Fail:", fail)

    f.close()


def grades():
    f = open("students.txt", "r")
    g = open("grades.txt", "w")

    for line in f:
        sid, name, marks = line.strip().split(",")
        marks = int(marks)

        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 40:
            grade = "C"
        else:
            grade = "F"

        print(sid, name, grade)
        g.write(f"{sid},{name},{grade}\n")

    f.close()
    g.close()

    print("Grades written to grades.txt")


# Main Program
while True:
    print("\n1.Display Records")
    print("2.Search Student")
    print("3.Topper & Lowest")
    print("4.Class Average")
    print("5.Pass/Fail Count")
    print("6.Generate Grades")
    print("7.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        display()

    elif ch == 2:
        search()

    elif ch == 3:
        topper_lowest()

    elif ch == 4:
        average()

    elif ch == 5:
        pass_fail()

    elif ch == 6:
        grades()

    elif ch == 7:
        break

    else:
        print("Invalid Choice")