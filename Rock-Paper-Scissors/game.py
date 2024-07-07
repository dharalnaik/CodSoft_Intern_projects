import random

a = 0  #Stores user's scores
b = 0  #Stores comp's scores

while True:
    user_input = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    comp_selection = random.choice(possible_actions)
    print(f"\nYou chose {user_input}, computer chose {comp_selection}.")

    if user_input == comp_selection:                         #When tied
        print(f"Both players selected {user_input}. It's a tie!")
    elif user_input == "rock":                               #User chose rock
        if comp_selection == "scissors":
            print("Rock smashes scissors! You win!")
            a=a+1
        else:
            print("Paper covers rock! You lose.")
            b=b+1
    elif user_input == "paper":                              #User chose paper
        if comp_selection == "rock":
            print("Paper covers rock! You win!")
            a=a+1
        else:
            print("Scissors cuts paper! You lose.")
            b=b+1
    elif user_input == "scissors":                           #User chose paper
        if comp_selection == "paper":
            print("Scissors cuts paper! You win!")
            a=a+1
        else:
            print("Rock smashes scissors! You lose.")
            b=b+1

    play_again = input("\nPlay again? (y/n): ")              #To play again
    if play_again.lower() != "y":
        print("The scores are: ")
        print("Your score: ", a)
        print("Computer score: ", b)
        if(a>b):
            print("\nYou won the game!")
        elif(a==b):
            print("\nThe game is tied.")
        else:
            print("\nComputer wins the game.")
        break
        