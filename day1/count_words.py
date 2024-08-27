# Function to count the number of words in a sentence
def count_words(sentence):
    # Split the sentence into words using whitespace as the delimiter
    words = sentence.split()
    
    # Return the number of words
    return len(words)

# Input: Sentence from the user
sentence = "Check divisibility up to the square root of the number"

# Count the number of words in the sentence
word_count = count_words(sentence)

# Output the result
print(f"The number of words in the sentence is: {word_count}")
