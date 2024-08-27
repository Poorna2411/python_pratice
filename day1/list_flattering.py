# Function to flatten a list of lists
def flatten_list(list_of_lists):
    # Use a list comprehension to flatten the list
    return [item for sublist in list_of_lists for item in sublist]

# Input: List of lists from the user
list_of_lists = [[1, 2], [3, 4], [5]]

# Flatten the list
flattened = flatten_list(list_of_lists)

# Output the result
print("Flattened list:", flattened)

