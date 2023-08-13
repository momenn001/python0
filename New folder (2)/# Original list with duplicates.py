# Original list with duplicates
original_list = [2, 4, 6, 4, 3, 2, 3, 4, 6, 7, 3, 9]

# Create a new list to store unique elements
unique_list = []

# Loop through the original list to remove duplicates
for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

# Print the list with duplicates removed
print("Original list:", original_list)
print("List with duplicates removed:", unique_list)
