# Correct answers
correct = ['A', 'C', 'B', 'D', 'A']

# Student answers
student = ['A', 'B', 'B', 'D', 'C']

score = 0
wrong_questions = []

# Check answers
for i in range(len(correct)):
    if correct[i] == student[i]:
        score += 1
    else:
        wrong_questions.append(i + 1)   # Question numbers start from 1

# Count correct and wrong answers
correct_count = score
wrong_count = len(correct) - score

# Calculate percentage
percentage = (score / len(correct)) * 100

# Determine pass or fail
if percentage >= 60:
    result = "Pass"
else:
    result = "Fail"

# Display results
print("Score:", score)
print("Incorrectly answered question numbers:", wrong_questions)
print("Correct answers:", correct_count)
print("Wrong answers:", wrong_count)
print("Percentage:", percentage, "%")
print("Result:", result)