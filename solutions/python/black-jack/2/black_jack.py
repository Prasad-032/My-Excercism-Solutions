def value_of_card(card):
    if card == 'J' or card == 'Q' or card == 'K':
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)

def higher_card(card_one, card_two):
    if value_of_card(card_one) == value_of_card(card_two):
        return card_one, card_two
    if value_of_card(card_one) < value_of_card(card_two):
        return card_two
    else:
        return card_one

def value_of_ace(card_one, card_two):
    val_one = 11 if card_one == 'A' else value_of_card(card_one)
    val_two = 11 if card_two == 'A' else value_of_card(card_two)
    if val_one + val_two + 11 <= 21:
        return 11
    else:
        return 1

def is_blackjack(card_one, card_two):
    if card_one == 'A' and card_two in ['10','J','Q','K']:
        return True
    if card_two == 'A' and card_one in ['10','J','Q','K']:
        return True
    else:
        return False

def can_split_pairs(card_one, card_two):
    return value_of_card(card_one) == value_of_card(card_two)

def can_double_down(card_one,card_two):
    return value_of_card(card_one) + value_of_card(card_two) in [9, 10, 11]
    