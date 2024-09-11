# made 30/8/24
# by francis igoe

import random

user_score = 0
opponent_score = 0

while True:
    # selects opponents hand
    rand = random.randint(1,3)
    if rand == 1:
        opponent_hand = "rock"
    elif rand == 2:
        opponent_hand = "paper"
    else:
        opponent_hand = "scisors"
    # lets the user select their hand with error handling
    user_hand = input("enter rock, paper or scisors: ")
    while user_hand != "rock" and user_hand != "scisors" and user_hand != "paper":
        print("enter a valid hand")
        user_hand = input("enter rock, paper or scisors: ")
    # calculates results, who won and adds to total win counts
    print("you chose ", user_hand, " , the opponent chose ", opponent_hand, ".")
    if user_hand == opponent_hand:
        print("its a tie") 
    elif user_hand == "rock" and opponent_hand == "scisors" or user_hand == "scisors" and opponent_hand == "paper" or user_hand == "paper" and opponent_hand == "rock":
        print("user wins!")
        user_score += 1
    else:
        print("opponent wins...")
        opponent_score += 1
    # checks if user wants to keep playing with error handling
    keep_playing = input("keep playing? (y/n)")
    while keep_playing != "y" or keep_playing != "n":
        keep_playing = input("keep playing? (y/n)")
    if keep_playing == "n":
        break

# shows final scores
print("final scores")
print("user score: ", user_score)
print("opponent score: ", opponent_score)