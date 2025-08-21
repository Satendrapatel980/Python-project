# Classis rock paper scissor game 

import random

options = ("rock", "paper", "scissors")


playing = True
while playing: 
    player = None
    computer = random.choice(options)
    while player not in options: 
        player = input("Enter a choice (rock, paper, scissor): ")


    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie")
    elif player == "rock" and computer =="scissors":
        print("You win")
    elif player == "paper" and computer =="rock":
        print("You win")
    elif player == "scissors" and computer =="paper":
        print("You win")
    else:
        print("You Loose!")
    
    play_gain = input("Play Again? (y/n): ").lower()
    if not play_gain == "y":
        playing = False

print("Thanks For Playing .... !")
