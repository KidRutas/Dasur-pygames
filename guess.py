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
# import random
# import os

# def guess():
#     options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     computer_guess = random.choice(options) # computer guess

#     try:
#         player_guess = int(input("Guess the number (1 - 10): "))
#     except ValueError:
#         print("Please enter a valid number.")
#         return None  # Return None if input is invalid

#     if player_guess < 1 or player_guess > 10:
#         print("Please input a number within parameters")
#         return None  # Return None if out of range

#     print(f"You chose {player_guess}, Computer chose {computer_guess}")
 
#     # if the player's guess is equal to the computer's guess
#     if player_guess == computer_guess:
#         print("You guessed right! Well done!")
#         return True  # Indicate a win
    
#     # else if the player's guess is less than the computer's guess
#     elif player_guess < computer_guess:
#         print("You guessed too low.")
#         return False  # Indicate a loss
#     else:
#         print("You guessed too high.")
#         return False  # Indicate a loss

# # this function returns number of wins and losses
# def wins_and_loss(wins_losses):
#     return f"Wins: {wins_losses['Wins']}, Losses: {wins_losses['Losses']}\n"

# # Main game loop
# wins_losses = {"Wins": 0, "Losses": 0} # stores wins and losses in dictionary data structure

# num_times = {"Number of plays": 0} # stores number of times a player has played the game

# file_csv = "Guess.csv"

# # Open the file in append mode initially
# with open(file_csv, "a+") as file:
#     # Write the headers only if the file is empty
#     file.seek(0)  # Move to the start of the file
#     read_line = file.readline()
#     if read_line == "":
#         if file.tell() == 0:  # Check if file is empty
#            file.write("Wins,Losses,Number of tries\n")

# while True:
#     result = guess()
#     if result is not None:
#         if result:  # If true, it's a win
#             wins_losses["Wins"] += 1
#         else:  # If false, it's a loss
#             wins_losses["Losses"] += 1
        
#         print(wins_and_loss(wins_losses))

#         # we want to count the number of times the player plays and then we will write it into our csv file
#         if result is not None:
#             num_times["Number of plays"] += 1

#         # Append the current result to the file
#         with open(file_csv, "a") as file:  # Open in append mode
#             file.write(f"{wins_losses['Wins']},{wins_losses['Losses']},{num_times['Number of plays']}\n")

#     again = input("Do you want to play again? (yes/no): ").strip().lower()
#     if again != 'yes':
#         print("Thanks for playing!")
#         break


import random
import csv

def guess():
    options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    computer_guess = random.choice(options)

    # Get valid input from the player
    while True:
        try:
            player_guess = int(input("Guess the number (1 - 10): "))
            if 1 <= player_guess <= 10:
                break  # Exit loop if valid
            else:
                print("Please input a number within the range.")
        except ValueError:
            print("Please enter a valid number.")

    print(f"You chose {player_guess}, Computer chose {computer_guess}")

    if player_guess == computer_guess:
        print("You guessed right! Well done!")
        return True
    elif player_guess < computer_guess:
        print("You guessed too low.")
        return False
    else:
        print("You guessed too high.")
        return False

def wins_and_loss(wins_losses):
    return f"Wins: {wins_losses['Wins']}, Losses: {wins_losses['Losses']}, Number of tries: {wins_losses['Number of plays']}\n"

# Function to read the last number of tries from the CSV file
def read_last_tries(file_csv):
    try:
        with open(file_csv, 'r') as file:
            reader = csv.reader(file)
            lines = list(reader)
            # If there's data, return the last recorded "Number of tries"
            if len(lines) > 1:  # Header and at least one row
                return int(lines[-1][2])  # The third column is "Number of tries"
            else:
                return 0  # If no data, start at 0
    except FileNotFoundError:
        return 0  # If file doesn't exist, start at 0

# Main game loop
file_csv = "Guess.csv"

# Read last number of tries from the file
last_tries = read_last_tries(file_csv)

wins_losses = {"Wins": 0, "Losses": 0, "Number of plays": last_tries}

# Open the CSV file once at the start
with open(file_csv, "a+") as file:
    file.seek(0)  # Move to start
    read_line = file.readline()
    if read_line == "":  # Write header if the file is empty
        file.write("Wins,Losses,Number of tries\n")

while True:
    result = guess()
    if result is not None:
        if result:
            wins_losses["Wins"] += 1
        else:
            wins_losses["Losses"] += 1

        # Increment number of tries for each play
        wins_losses["Number of plays"] += 1

        # Append result to CSV
        with open(file_csv, "a") as file:
            file.write(f"{wins_losses['Wins']},{wins_losses['Losses']},{wins_losses['Number of plays']}\n")

        print(wins_and_loss(wins_losses))

    again = input("Do you want to play again? (yes/no): ").strip().lower()
    if again != 'yes':
        print("Thanks for playing!")
        print(wins_and_loss(wins_losses))  # Final stats
        break

