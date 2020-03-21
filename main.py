from os import system
from random import seed
from random import randint
seed(1)

# Variables
possible_actions    = ["rock","paper","scissors"]
computer_decision   = randint(0,3)
user_wins           = 0
computer_wins       = 0
valid_action        = False
game                = True

# Clear screen after every new game
def clearScreen():
    system('clear')

# Display current score
def currentScores():
    global user_wins
    global computer_wins

    print("\nComputer score: ", computer_wins, "\n" +
          "User score: ", user_wins, "\n")

# Determine winning conditions
def winMatch(user_action, computer_action):
    global user_wins
    global computer_wins

    if valid_action == True and possible_actions.index(computer_action) < possible_actions.index(user_action):
        print("User WINS!")
        user_wins += 1
    elif  valid_action == True and possible_actions.index(computer_action) > possible_actions.index(user_action):
        print("Computer WINS!")
        computer_wins += 1
    elif valid_action == True and possible_actions.index(computer_action) == possible_actions.index(user_action):
        print("It's a tie! No wins!")

    # Show current score
    currentScores()

# Start game
while game == True:
    # Prompt user for input
    user_action = input("Enter decision: ")
    # Computer selects its action randomly
    computer_action = possible_actions[computer_decision]

    # Verify input is a valid action
    for action in possible_actions:
        if user_action == action:
            print("VALID ACTION")
            valid_action = True
            break

    # Determine if winning conditions
    winMatch(user_action, computer_action)

    # Prompt user to continue playing
    continue_game = input("Continue playing (yes/no): ")
    if continue_game == "yes" or continue_game == "Yes" or continue_game == "y" or continue_game == "Y":
        game == True
        # Reset valid actions
        valid_action = False
        # Clear screen
        clearScreen()
    elif continue_game == "no" or continue_game == "No" or continue_game == "n" or continue_game == "N":
        game == False
        break
    else:
        print("Not a valid choice!")