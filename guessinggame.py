import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    target_number = random.randint(1, 50)
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:
        guess = input(f"\nAttempt {attempts + 1}/{max_attempts} - Guess a number between 1 and 50: ")
        
        try:
            user_guess = int(guess)
            attempts += 1

            if user_guess == target_number:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
            elif user_guess < target_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if attempts == max_attempts:
        print(f"\nGame Over! The correct number was {target_number}.")

number_guessing_game()
