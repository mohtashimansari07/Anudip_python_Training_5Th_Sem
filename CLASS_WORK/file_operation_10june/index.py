"""Classwork : To read the data from file and display the following:
1. No. of Vowels in file.
2. No. of characters into the file.
3. No. of lines into the file."""

# Create and write data into the file
f = open("sample.txt", "w")

f.write("Hello World\n")
f.write("Python Programming\n")
f.write("File Handling\n")
f.write("I am Mohtashim\n")
f.write("I am learning Python\n")

f.close()

# Open the file in read mode
f = open("sample.txt", "r")

vowels = 0
characters = 0
lines = 0

# Read the file line by line
for line in f:
    lines += 1

    for ch in line:
        characters += 1

        if ch.lower() in "aeiou":
            vowels += 1

f.close()

print("Number of vowels:", vowels)
print("Number of characters:", characters)
print("Number of lines:", lines)