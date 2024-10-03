# Create a game where the computer randomly selects a number, 
# and the player has to guess it. 
# Provide hints like "too high" or "too low."

# import random

# def guess():
    # Player's guess
    # global player_guess, computer_guess
    # player_guess = int(input("Guess the number 1 - 10: "))
    # options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # incase the player enters a number outside the options list
    # this is will return an error message
    # if player_guess < 1 or player_guess > 10:
    #     print("Please input number within parameters")
    #     return
    
    # This is guess of the computer
    # computer_guess = random.choice(options)
    
    # global wnl
    # wnl = {"Player": player_guess,
    #        "Computer": computer_guess}

    # if player_guess == computer_guess:
    #     print("You guessed right! Well done\n" + f"You chose {player_guess}, Computer chose {computer_guess}")
    # elif player_guess < computer_guess:
    #     print("You guessed too low\n" + f"You chose {player_guess}, Computer chose {computer_guess}")
    # elif player_guess > computer_guess:
    #     print("You guessed too high\n" + f"You chose {player_guess}, Computer chose {computer_guess}")

# I wanna count how many Wins and Loses I have
# def wins_and_loss(player, computer):
#     wins = 0
#     loss = 0

#     wins_n_loss = {"Wins": wins,
#                    "Loss": loss}
    
#     if player == computer:
#         wins_n_loss["Wins"] += 1
#         print("Wins and Loss: ", wins_n_loss["Wins"])
#     elif player == computer:
#         wins_n_loss["Loss"] += 1
#         print("Wins and Loss: " , wins_n_loss["Loss"])

# wins_and_loss(guess(wnl["Player"], wnl["Computer"]))

# Chatgpt improved code 
import random
import os

def guess():
    options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    computer_guess = random.choice(options) # computer guess

    try:
        player_guess = int(input("Guess the number (1 - 10): "))
    except ValueError:
        print("Please enter a valid number.")
        return None  # Return None if input is invalid

    if player_guess < 1 or player_guess > 10:
        print("Please input a number within parameters")
        return None  # Return None if out of range

    print(f"You chose {player_guess}, Computer chose {computer_guess}")
 
    # if the player's guess is equal to the computer's guess
    if player_guess == computer_guess:
        print("You guessed right! Well done!")
        return True  # Indicate a win
    
    # else if the player's guess is less than the computer's guess
    elif player_guess < computer_guess:
        print("You guessed too low.")
        return False  # Indicate a loss
    else:
        print("You guessed too high.")
        return False  # Indicate a loss

# this function returns number of wins and losses
def wins_and_loss(wins_losses):
    return f"Wins: {wins_losses['Wins']}, Losses: {wins_losses['Losses']}\n"

# Main game loop
wins_losses = {"Wins": 0, "Losses": 0} # stores wins and losses in dictionary data structure

num_times = {"Number of plays": 0} # stores number of times a player has played the game

file_csv = "Guess.csv"

# Open the file in append mode initially
with open(file_csv, "a+") as file:
    # Write the headers only if the file is empty
    file.seek(0)  # Move to the start of the file
    read_line = file.readline()
    if read_line == "":
        if file.tell() == 0:  # Check if file is empty
           file.write("Wins,Losses,Number of tries\n")
    

while True:
    result = guess()
    if result is not None:
        if result:  # If true, it's a win
            wins_losses["Wins"] += 1
        else:  # If false, it's a loss
            wins_losses["Losses"] += 1
        
        print(wins_and_loss(wins_losses))

        # we want to count the number of times the player plays and then we will write it into our csv file
        if result is not None:
            num_times["Number of plays"] += 1

        # Append the current result to the file
        with open(file_csv, "a") as file:  # Open in append mode
            file.write(f"{wins_losses['Wins']},{wins_losses['Losses']},{num_times['Number of plays']}\n")

    again = input("Do you want to play again? (yes/no): ").strip().lower()
    if again != 'yes':
        print("Thanks for playing!")
        break
