def can_vote(nationality, age):
    if nationality.lower() == "jordanian" and age > 18:
        return True
    else:
        return False

def main():
    nationality = input("Enter your nationality: ")
    age = int(input("Enter your age: "))

    if can_vote(nationality, age):
        print("You have access to vote in the elections.")
    else:
        print("You do not have access to vote in the elections.")

if __name__ == "__main__":
    main()
