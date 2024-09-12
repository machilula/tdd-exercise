VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    score = 0 
    if len(hand) in range(2,6):
        for card in hand:
            if card in VALID_CARDS:
                if isinstance(card, int):
                    score += card
                elif card == 'King' or card == 'Queen':
                    score += 10
                elif card == 'Ace' and score < 10:
                    score += 1
                elif card == 'Ace' and score <= 10:
                    score += 10
            else:
                print("face card not valid")
    else:
        print("invalid hand")
        return False

    if score == 21:
        print ("you won!")
        return score
    elif score < 21:
        print("too low!")
        return score
    else:
        print("bust!")
    return score
    




    


