import random

def player_amount():

    print("\nHow many players are there?")
    player_amount = int(input())

    if player_amount >= 10:
        print("That's too many players!")
        player_amount()

    if player_amount <= 2:
        print("That's not enough players!")
        player_amount()

    #creation of 1 class per player
    for 