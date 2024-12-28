import random

def quiz_competition():
    # Welcome message
    print("Welcome to the Quiz Competition!")
    print("You will be given a list of numbers. Try to guess the one chosen by the judge!")

    # Input list of numbers from the user
    numbers = input("Enter a list of numbers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]

    # Randomly choose a number from the list
    chosen_number = random.choice(numbers)

    # Start the guessing game
    while True:
        try:
            guessed_number = int(input("Guess the number chosen by the judge: "))
            if guessed_number > chosen_number:
                print("Your guess is too high. Try again!")
            elif guessed_number < chosen_number:
                print("Your guess is too low. Try again!")
            else:
                print("Congratulations! You guessed the correct number.")
                break
        except ValueError:
            print("Please enter a valid integer.")

# Run the game
if __name__ == "__main__":
    quiz_competition()
