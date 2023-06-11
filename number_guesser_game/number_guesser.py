import random

def main():
    replay = "Y"
    while replay == "Y":
        welcome_user()
        lower_range, upper_range = get_range()
        play_game(lower_range, upper_range)
        replay = input('Play again? Type "Y" for yes or "N" for no: ')
    print("\nThank you for playing!")

def welcome_user():
    print("Welcome to the Number Guesser Game!\n"
          "Rules:\n"
          "In this game, you will be trying to guess a random number between 2 values of your choice.\n"
          "You will be given hints that say whether the number is higher or lower than your guess.\n"
          "Good Luck!")

def get_range():
    print("\nChoose the range of numbers you want to play with")
    lower_range = int(input("\nFrom: "))
    upper_range = int(input("To: "))
    return lower_range, upper_range

def get_random_number(lower, upper):
    return random.randint(lower, upper)

def play_game(lower, upper):
    rand_num = get_random_number(lower, upper)
    while True:
        try:
            user_guess = int(input("Guess the number: "))
            if user_guess == rand_num:
                print("\nYou Win!!!")
                break
            elif user_guess > rand_num:
                print("\nToo High!")
            else:
                print("\nToo Low!")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

main()

    




