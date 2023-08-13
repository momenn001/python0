# Generate a random number between 1 and 100
import random
target_number = random.randint(1, 100)

# Number of allowed guesses
allowed_guesses = 3
guess_count = 0

while guess_count < allowed_guesses:
    # Get user's guess
    user_guess = int(input("Guess a number between 1 and 100: "))
    
    # Increment the guess count
    guess_count += 1
    
    # Check if the guess is correct
    if user_guess == target_number:
        print("Correct!")
        break
    elif guess_count == allowed_guesses:
        print("Game over. You've used all your guesses. The correct number was", target_number)
    else:
        print("Try again!")

print("Thanks for playing!")
