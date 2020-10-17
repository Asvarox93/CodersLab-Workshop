from random import shuffle

# Generate lotto numbers and return 6 of them
def generate_lotto_numbers(func):
    lotto_numbers = [i for i in range(1,49)]
    shuffle(lotto_numbers)

    def get_lotto_numbers():
        func(lotto_numbers[:6])

    return get_lotto_numbers


# Get 6 user numbers and then check if guessed lotto numbers
@generate_lotto_numbers
def lotto_game(lotto_numbers):
    while True:
        try:
            guess_numbers = list(map(int, input("Enter 6 different numbers from between 1-49: ").strip().split()))
        except ValueError:
            print("One ore more values are not a number!")
            continue

        if len(guess_numbers) > 6 or len(guess_numbers) < 6:
            print("The are more or less numbers then 6!")
            continue
        if len(guess_numbers) != len(set(guess_numbers)):
            print("The are two or more same numbers!")
            continue

        for n in guess_numbers:
            if n > 49 or n < 1:
               print("There is a number not in range 1-49!")
               break
        else:
            guess_numbers.sort()
            print("Your numbers: ", guess_numbers)
            print("Lotto numbers: ", lotto_numbers)

            quessed_number = set(guess_numbers) & set(lotto_numbers)
            print("Guessed numbers: ", len(quessed_number))
            break


lotto_game()
