def get_letter_grade(grade):
    if 90 <= grade <= 100:
        return "A"
    elif 80 <= grade < 90:
        return "B"
    elif 70 <= grade < 80:
        return "C"
    elif 60 <= grade < 70:
        return "D"
    elif 0 <= grade < 60:
        return "F"
    else:
        return "Invalid grade"

def main():
    try:
        grade = int(input("Enter the student's grade (0-100): "))
        if 0 <= grade <= 100:
            letter_grade = get_letter_grade(grade)
            print(f"The student's letter grade is: {letter_grade}")
        else:
            print("Invalid input: Grade should be between 0 and 100.")
    except ValueError:
        print("Invalid input: Please enter a valid number.")

if __name__ == "__main__":
    main()
