# Get user input for birth year
birth_year = int(input("Please enter your birth year: "))

# Get the current year
import datetime
current_year = datetime.datetime.now().year

# Calculate age
age = current_year - birth_year

# Print the result
print("Your age is:", age, "years")
