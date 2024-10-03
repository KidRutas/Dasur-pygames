# Let's create a rock paper scissors game

import random

def game():
   player_choice = str(input("Choose between these (Rock, Paper, Scissors): ").lower())
   options = ["rock", "paper", "scissors"]
   computer_choice = random.choice(options)
   choices = {"player": player_choice, 
              "computer": computer_choice
              }
   return choices


def check_win(player, computer):
     print(f"You chose {player}, computer chose {computer}")
     
     if player == computer:
         print("It's a tie")
     elif player != computer:
         print(f"You lose!")
         
     
choices = game()
check_win(choices["player"], choices["computer"])