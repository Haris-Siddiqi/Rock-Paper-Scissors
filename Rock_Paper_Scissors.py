# Rock, Paper, Scissors Game!

# Import random library for choosing a random number
import random


def rock_paper_scissors():
    '''(NoneType) -> NoneType
    A rock, paper, scissors game. Generates a move for the computer
    and prompts the player for a move and compares their moves. Integers
    are used for each move, rock being 1, paper being 2, and scissors being
    3.
    REQ:
    >>>
    '''
    # Generates a random move for the computer
    cpu_choice = random.randint(1, 3)
    # Prompts the user for input
    user_choice = input(
        "\nPlease type 1 for Rock, 2 for Paper, or 3 for Scissors: "
        )
    # Ensures input is in acceptable format, otherwise resarts game
    input_type_checker(user_choice)
    # Converts chioce to integer once format is correct
    user_choice = int(user_choice)
    # Compares choices and decides between loss, win, and draw
    print()
    compare(user_choice, cpu_choice)


def input_type_checker(char):
    ''' (str) -> NoneType
    This function checks whether the User's input is in the acceptable
    format ie. 1 or 2 or 3. If not, an error message is displayed and the
    game restart.
    '''
    options = ['1', '2', '3']
    correct = False
    # Checks whether the input matches any of the acceptable inputs and changes
    # correct to True if it does
    count = 0
    while count < 3:
        if char == options[count]:
            correct = True
        count += 1
    # Game restarts if input does not match
    if correct is False:
        print("\nType either 1 or 2 or 3. Try again. ")
        rock_paper_scissors()


def compare(user, cpu):
    ''' (int, int) -> NoneType
    Compares user and cpu choices and calls on tie, win or lose functions.
    '''
    if user == cpu:
        tie()
    elif user == 1 and cpu == 3:
        win()
    elif user == 2 and cpu == 1:
        win()
    elif user == 3 and cpu == 2:
        win()
    elif cpu == 1 and user == 3:
        lose()
    elif cpu == 2 and user == 1:
        lose()
    elif cpu == 3 and user == 2:
        lose()


def tie():
    ''' (NoneType) -> NoneType
    Prints message and executes try_again function.
    '''
    print("Hmm... tie game.")
    try_again()


def win():
    ''' (NoneType) -> NoneType
    Prints message and executes try_again function.
    '''
    print("Congrats, you won!")
    try_again()


def lose():
    ''' (NoneType) -> NoneType
    Prints message and executes try_again function.
    '''
    print("Sorry, it looks like you lost... ")
    try_again()


def try_again():
    ''' (NoneType) -> NoneType
    Gives user option to play again or quit.
    '''
    choice = input("\nWould you like to play again? (y / n) ")
    if choice == "y":
        rock_paper_scissors()
    elif choice == "n":
        print("\nThanks for playing!\n")
        quit()
    else:
        print("Try again.")
        try_again()

# Welcome message then execute game
print("\nWelcome to Rock, Paper, Scissors!")
rock_paper_scissors()
