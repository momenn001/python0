# Get user input for weight in kilograms
weight_kg = float(input("Please enter your weight in kilograms: "))

# Conversion factor: 1 kg = 2.20462 lbs
conversion_factor = 2.20462

# Convert weight to pounds
weight_lbs = weight_kg * conversion_factor

# Print the result
print("Your weight in pounds is:", weight_lbs, "lbs")
