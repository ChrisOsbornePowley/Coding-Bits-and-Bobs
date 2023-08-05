#A game of Pig made by following TechWithTim's tutorial: https://youtu.be/21FnnGKSRZo 

import random

#Roll function rolls between 1 and 6 and returns the value 
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

#Loop to select the number of players
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            print(f"You've chosen {players} players.")
            break
        else:
            print("Number must be between 2 and 4.")
    else:
        print("Enter a number value only.")

#The starting max score to aim for and a list to store the player scores
max_score = 10
player_scores = [0 for _ in range(players)]

#Loop to play the game, looping through each player asking them if they wish to roll. If they roll a 1, turn ends and score is not added.
#If they roll anything else, it is added to the total when their turn ends.
#Runs through all players until one of the player scores is greater than the max score, at the end of that round of turns.
while max(player_scores) < max_score:
    
    for player_idx in range(players):
        print(f"\nPLAYER {player_idx + 1}'s turn has started.")
        print(f"PLAYER {player_idx + 1}'s total score is {player_scores[player_idx]}.\n")
        current_score = 0 
        

        while True:
            should_roll = input("Would you like to roll? (y)? ")
            if should_roll.lower() != "y":
                ("Turn finished.")
                break
            
            value = roll()
            if value == 1:
                print("You rolled a 1. Turn OVER!")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a {value}")
            
            print(f"Your score is {current_score}")
        
        player_scores[player_idx] += current_score
        print(f"Your total score is {player_scores[player_idx]}")

#Report the winning player and their score.
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print(f"\nGAME OVER! \nPlayer number {winning_idx + 1} is the winner with a score of {max_score}")