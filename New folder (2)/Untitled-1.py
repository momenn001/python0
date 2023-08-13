def calculate_age(birth_year):
    current_year = 2023  # Assuming the current year is 2023
    age = current_year - birth_year
    return age

def main():
    birth_year = int(input("Enter your birth year: "))
    age = calculate_age(birth_year)

    print(f"You are {age} years old.")

if __name__ == "__main__":
    main()