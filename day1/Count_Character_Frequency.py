# Function to count the frequency of each character in a string
def count_char_frequency(s):
    frequency = {}  # Dictionary to store character frequencies
    
    # Loop through each character in the string
    for char in s:
        if char in frequency:
            frequency[char] += 1  # Increment the count for the character
        else:
            frequency[char] = 1  # Initialize the count for the character
    
    return frequency

# Input: String from the user
input_string = "poorna"

# Count the frequency of each character in the string
char_frequency = count_char_frequency(input_string)

# Output the result
print("Character frequencies:")
for char, freq in char_frequency.items():
    print(f"'{char}': {freq}")
