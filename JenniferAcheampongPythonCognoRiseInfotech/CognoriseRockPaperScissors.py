import random

print("LET'S PLAY ROCK, PAPER, AND SCISSORS\n..................................")
print("\t\t\t\tUSER MANUAL\n...........................................")

print('A USER ENTERS ANY OF THE THREE ITEMS AND COMPARES SELECTION TO COMPUTER\'S CHOICE'
      '\nUPON SAME SELECTION, RESULT DISPLAYS AS TIE, ELSE WIN OR LOSE'
      '\nROCK BEATS SCISSORS, SCISSORS BEAT PAPER, AND PAPER BEATS ROCK\n ')

print("READY, LET'S GO!")


def play_game():
    items = ["rock", "paper", "scissors"]

    User_Input = input("Enter any item (rock, paper, scissors): ")
    if User_Input not in items:
        print("Invalid selection. Please enter rock, paper, or scissors.")
        play_game()  # Restart the game if input is invalid
        return

    Computer_Choice = random.choice(items)

    print(f"USER: {User_Input}")
    print(f"COMPUTER: {Computer_Choice}")

    if User_Input == Computer_Choice:
        print("TIE")
    elif (
            (User_Input == "rock" and Computer_Choice == "scissors")
            or
            (User_Input == "scissors" and Computer_Choice == "paper")
            or
            (User_Input == "paper" and Computer_Choice == "rock")
    ):
        print("WIN")
    else:
        print("LOSE")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':

        play_game()


# Start the game
play_game()