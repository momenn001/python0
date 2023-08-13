# Initialize an empty list
numeric_list = []

# Loop to fill the list
while True:
    user_input = input("Enter a number (or 'quit' to stop): ")
    
    if user_input.lower() == "quit":
        break
    
    try:
        number = float(user_input)
        numeric_list.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number or 'quit'.")

# Display the length of the list
print("Length of the list:", len(numeric_list))

# Sort the list in ascending order
numeric_list.sort()
print("Sorted list:", numeric_list)
