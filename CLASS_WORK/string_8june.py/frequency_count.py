#WAP to input the sentence and display the frequendcy of vowels which are present in the sentence ignoring the case .
# Take the input sentence from the user
sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
frequency = {}
#using for loop to count the frequency of vowels in the sentence
for char in sentence:
    if char in vowels:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1 
print("Frequency of vowels in the sentence:")
#using for loop to display the frequency of each vowel
for vowel, count in frequency.items():  
    print(f"{vowel}: {count}") 
