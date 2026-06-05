# This program analyzes the performance of students based on their marks.
marks=[78,45,92,35,88,40,99,56]

#dislay all students
passed_students = []
failed_students = 0
highest = 0
lowest = 0
merit = []

for i in marks[1:]:  #iterating through the list of marks
    if i >= 40:
        passed_students.append(i)  #passed students are added to the list
    else:
        failed_students += 1       #failed count is incremented


    #highest marks
    if i>highest:
        highest = i
    #lowest marks
    if i<lowest or lowest == 0:
        lowest = i
    #merit list
    if i>75:
        merit.append(i)    
         

#display results
print("Passed Students:", passed_students)
print("Failed Students:", failed_students)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Merit Students:", merit)
