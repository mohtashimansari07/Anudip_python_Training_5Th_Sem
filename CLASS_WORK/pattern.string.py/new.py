# Write a program to input a sentence from user and count the no of special characters present in the sentence.
sentence = input("Enter a sentence: ")
special_char = "!@#$%^&*()_+-=[]{}|;':\",.<>/?`~"
count = 0
for char in sentence:
    if char in special_char:
        count += 1
print("Number of special characters in the sentence:", count)
