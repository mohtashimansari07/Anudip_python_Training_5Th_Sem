# Student Performance Analytics System

students = {}

# Input details of 30 students
for i in range(30):
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    students[sid] = {"name": name, "marks": marks}

# 1. Display all student records
print("\nStudent Records:")
for sid in students:
    print(sid, students[sid])

# 2. Search a student using Student ID
sid = input("\nEnter Student ID to search: ")

if sid in students:
    print("Record Found:", students[sid])
else:
    print("Student not found")

# 3. Add a new student
sid = input("\nEnter new Student ID: ")
name = input("Enter Name: ")
marks = int(input("Enter Marks: "))

students[sid] = {"name": name, "marks": marks}

# 4. Update marks of an existing student
sid = input("\nEnter Student ID to update marks: ")

if sid in students:
    students[sid]["marks"] = int(input("Enter new marks: "))
    print("Marks updated")
else:
    print("Student not found")

# 5. Delete a student
sid = input("\nEnter Student ID to delete: ")

if sid in students:
    del students[sid]
    print("Student deleted")
else:
    print("Student not found")

# 6. Find topper and lowest scorer
topper = ""
lowest = ""

for sid in students:
    if topper == "" or students[sid]["marks"] > students[topper]["marks"]:
        topper = sid

    if lowest == "" or students[sid]["marks"] < students[lowest]["marks"]:
        lowest = sid

print("\nTopper:", topper, students[topper])
print("Lowest Scorer:", lowest, students[lowest])

# 7. Calculate class average
total = 0

for sid in students:
    total += students[sid]["marks"]

average = total / len(students)

print("\nClass Average:", average)

# 8. Count pass and fail students
pass_count = 0
fail_count = 0

for sid in students:
    if students[sid]["marks"] >= 50:
        pass_count += 1
    else:
        fail_count += 1

print("Pass Students:", pass_count)
print("Fail Students:", fail_count)

# 9. Generate grades
print("\nGrades:")

for sid in students:
    marks = students[sid]["marks"]

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "F"

    print(sid, students[sid]["name"], ":", grade)

# 10. Display students scoring above average
print("\nStudents Scoring Above Average:")

for sid in students:
    if students[sid]["marks"] > average:
        print(sid, students[sid])

# 11. Display top 5 performers
print("\nTop 5 Performers:")

temp = students.copy()

for i in range(5):
    top = ""

    for sid in temp:
        if top == "" or temp[sid]["marks"] > temp[top]["marks"]:
            top = sid

    print(top, temp[top])

    del temp[top]

# 12. Create scholarship dictionary (marks > 85)
scholarship = {}

for sid in students:
    if students[sid]["marks"] > 85:
        scholarship[sid] = students[sid]

print("\nScholarship Students:")
for sid in scholarship:
    print(sid, scholarship[sid])