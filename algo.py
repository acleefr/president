#import random
import random

# card distribution

print("")
print("Welcome to the card distribution program!")
print("")
print("How many players are there?")

num_players = int(input())

if num_players >= 10:
    print("That's too many players!")
    exit()

if num_players <= 2:
    print("That's not enough players!")
    exit()

#creation of the cards

print("")
print("Creating the cards...")
print("")

a = 0
cards = [0] * 52

for i in range(1, 5):
    for j in range(1, 14):
        if i == 1:
            cards[a] = "Spade" + str(j)
        elif i == 2:
            cards[a] = "Heart" + str(j)
        elif i == 3:
            cards[a] = "Club" + str(j)
        else:
            cards[a] = "Diamond" + str(j)
        a = a + 1

print(cards)

#shuffle the cards

print("")
print("Shuffling the cards...")
print("")

random.shuffle(cards)
print(cards)

#distribute the cards

print("")
print("Distributing the cards...")
print("")

card_amount = 52 / num_players
card_amount = int(card_amount)
print("there are " + str(card_amount) + " cards per player ")

k = 0
m = 0
player_cards = []

while m < num_players:
        player_cards.insert(m, "player" + str(m + 1))
        m = m + 1


m = 0
o = 0
p = 0

player = {}

while k < 51:
    while p < card_amount:
        while m < num_players:
            player["player{0}".format(m+1)] = [] * card_amount
            print(k)
            player["player{0}".format(m+1)].insert(p,cards[k])
            m = m + 1
            k = k + 1
        m = 0
        p = p + 1
        
    


print(player)   