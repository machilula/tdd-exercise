VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    score = 0 
    for card in hand:
        if card in VALID_CARDS:
            score += card
            if card == 'Ace' and score <=10:
                score += ace_is_eleven
            else:
                score += ace_is_one


    ace_is_eleven = 11
    ace_is_one = 1

    if score <= 10:
        score += ace_is_eleven
    else:
        score += ace_is_one




    return score