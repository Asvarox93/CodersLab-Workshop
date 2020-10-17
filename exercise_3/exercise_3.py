# Get user answer and checking if is one of choose
def get_user_answer():
    answers = ["to small", "to big", "you win"]

    while True:
        user_answer = input('Your answer: "to small", "to big", "you win"\n').lower()
        if user_answer in answers:
            return user_answer


# Main loop - checking if PC guess user number
def guess_game():
    print("Imagine number between 0 and 1000 and i will guess it")
    print("Press enter to start")
    input()
    min_number = 0
    max_number = 1000
    user_answer = ''

    while user_answer != 'you win':
        guess = int((max_number - min_number) / 2) + min_number

        while True:
            print("Guessing: ", guess)
            user_answer = get_user_answer()
            if user_answer == 'you win':
                print('I guessed you number!')
                break
            elif user_answer == 'to big':
                max_number = guess
                break
            elif user_answer == 'to small':
                min_number = guess
                break
            else:
                print("Stop cheating!")


guess_game()
