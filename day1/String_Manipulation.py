"""
Write a Python program that takes a sentence as input, 
counts the number of vowels in the sentence, and prints the count.
"""

# Function to count vowels in a given sentence
def count_vowels(sentence):
    vowels = "aeiouAEIOU"  # All lowercase and uppercase vowels
    count = 0
    
    # Loop through each character in the sentence
    for char in sentence:
        if char in vowels:  # Check if the character is a vowel
            count += 1
    
    return count

# Input: Sentence from the user
sentence = input("Enter a sentence: ")

# Count the number of vowels in the sentence
vowel_count = count_vowels(sentence)

# Output the result
print(f"The number of vowels in the sentence is: {vowel_count}")
