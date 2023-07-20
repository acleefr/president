while k < 52:
    while o < card_amount:
        while m < num_players:
            player["player{0}".format(m+1)] = [] * card_amount
            player["player{0}".format(m+1)].insert(cards[p+1])
            p = p + 1
            m = m + 1
        o = o + 1
    m = 0
    k = k + 1