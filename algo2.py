import random

def num_players():                        # defining the amount of player
    
    print("\nHow many players are there?")
    num_players = int(input())

    if num_players >= 10:
        print("That's too many players!")
        num_players()

    if num_players <= 2:
        print("That's not enough players!")
        num_players()
    
    card_creation(num_players)

def card_creation(num_players):              # creation of the cards
    
    print("\ncard distribution")

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

    return card_shuffled(cards, num_players)

def card_shuffled(cards, num_players):                              # we shuffle the cards
    
    print("\ncard shuffling")
    random.shuffle(cards)

    print("\nshuffle done : ")
    print(cards)

    card_amount = 52 // num_players                                 # Calculate card amount inside this function
    return card_counting(cards, card_amount, num_players)

def card_counting(cards, card_amount, num_players):                #count the cards
    
    print("\nDistributing the cards...")
    print(f"there are {card_amount} cards per player ")

    return player_creation(cards, card_amount, num_players)

def player_creation(cards, card_amount, num_players):
    player_cards = []
    player_id = 0  # Initialized player_id

    while player_id < num_players:
            player_cards.insert(player_id, "player" + str(player_id + 1))
            player_id = player_id + 1
    
    return card_distribution(cards, card_amount, num_players, player_cards)

def card_distribution(cards, card_amount, num_players, player_cards):                #distribute the cards
    
    player = {}
    card_id = 0  # Initialized card_id
    deck_id = 0  # Initialized deck_id
    player_id = 0  # Initialized player_id
    
    while player_id < num_players:
        player[player_cards[player_id]] = []  # Initialize each player's card list as an empty list
        player_id = player_id + 1

    player_id = 0  # Reset player_id

    while card_id < len(cards):   # use len(cards) instead of hardcoding 51
        
        while deck_id < card_amount:
            
            while player_id < num_players and card_id < len(cards):  # Added card_id check to ensure we don't exceed cards list length
                
                player[player_cards[player_id]].append(cards[card_id])  # Append the card to the player's card list
                player_id = player_id + 1
                card_id = card_id + 1

            player_id = 0
            deck_id = deck_id + 1

    player_id = 0  # Reset player_id

    while player_id < num_players:
        print("player", player_id+1, " : ")
        print(player[player_cards[player_id]])
        print("\n")
        player_id = player_id + 1

    return first_round(player_cards, player, num_players)

def first_round(player_cards, player, num_players):
    
    print("\n")
    print("first round")

    playing_player = 0

    #display the card of player 1
    print(player[player_cards[playing_player]])

    #display the first card of player 1
    print()

num_players()