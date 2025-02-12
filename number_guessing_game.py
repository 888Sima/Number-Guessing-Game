import random

def guess_number_game():
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100
    number_to_guess = random.randint(lower_bound, upper_bound)

    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")

    # Initialize the number of attempts
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            # Get the player's guess
            guess = int(input("Enter your guess: "))

            # Check if the guess is within the valid range
            if guess < lower_bound or guess > upper_bound:
                print(f"Please guess a number between {lower_bound} and {upper_bound}.")
                continue

            # Increase the number of attempts
            attempts += 1

            # Check if the guess is correct
            if guess == number_to_guess:
                print(f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempts} attempts.")
                break
            elif guess < number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    if attempts == max_attempts and guess != number_to_guess:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")

# Run the game
guess_number_game()
