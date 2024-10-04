# Create a game where the computer randomly selects a number, 
# and the player has to guess it. 
# Provide hints like "too high" or "too low."

import random
import csv

def guess():
    # Computer makes a random guess
    computer_guess = random.randint(1, 10)

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
        return True, computer_guess, player_guess
    elif player_guess < computer_guess:
        print("You guessed too low.")
        return False, computer_guess, player_guess
    else:
        print("You guessed too high.")
        return False, computer_guess, player_guess

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
                return int(lines[-1][4])  # The fifth column is "Number of tries"
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
        file.write("Wins,Losses,Computer guess, Player guess, Number of tries\n")

while True:
    result, computer_guess, player_guess = guess()
    if result is not None:
        if result:
            wins_losses["Wins"] += 1
        else:
            wins_losses["Losses"] += 1

        # Increment number of tries for each play
        wins_losses["Number of plays"] += 1

        # Append result to CSV
        with open(file_csv, "a") as file:
            file.write(f"{wins_losses['Wins']},{wins_losses['Losses']},{computer_guess},{player_guess},{wins_losses['Number of plays']}\n")

        print(wins_and_loss(wins_losses))

    again = input("Do you want to play again? (yes/no): ").strip().lower()
    if again != 'yes':
        print("Thanks for playing!")
        print(wins_and_loss(wins_losses))  # Final stats
        break
