# Write a program to input a sentence from user and count the no of special characters present in the sentence.
#Take the input sentence from the user and store it in a variable.
sentence = input("Enter a sentence: ");
#define a string of special characters to check .
special_char = "!@#$%^&*()_+-=[]{}|;':\",.<>/?`~";
count = 0
#using for loop to iterate through each character in the sentence and check if it is a special character .
for char in sentence:
    if char in special_char:
        count += 1
print("Number of special characters in the sentence:", count)
