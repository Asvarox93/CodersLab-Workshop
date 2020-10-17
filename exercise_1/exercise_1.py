from random import randint


# Generate random number between 1-100 for guessing game
def generate_number(func):
    random_number = randint(1, 100)

    def guess_number():
        func(random_number)

    return guess_number


# Ask user for the number and then checking if he guessed the guess number
@generate_number
def guessing_game(guess_number):
    while True:
        try:
            guess = int(input("Guess the number: "))

            if guess == guess_number:
                print('You win!')
                break
            elif guess >= guess_number:
                print('To big!')
            else:
                print('To small!')
        except ValueError:
            print("It's not a number!")


guessing_game()
