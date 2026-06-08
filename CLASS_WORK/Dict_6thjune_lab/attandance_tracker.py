# Empty dictionary to store attendance
attendance = {}

# Number of students
n = 30

# Take attendance
for i in range(n):
    roll_no = input("Enter student Roll No: ")
    status = input("Present or Absent (P/A): ")

    attendance[roll_no] = status

# Display attendance
print("\nAttendance Record:")
for roll_no, status in attendance.items():
    print(f"Roll No: {roll_no}, Status: {status}")
