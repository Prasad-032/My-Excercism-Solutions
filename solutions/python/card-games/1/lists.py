def get_rounds(number):
    return  [number, number + 1, number + 2]

def concatenate_rounds(round_1, round_2):
    return round_1 + round_2

def list_contains_round(rounds, number):
    return number in rounds

def card_average(hand):
    return sum(hand) / len(hand)

def approx_average_is_average(hand):
    avg_1_last = (hand[0] + hand[-1]) / 2
    median = hand[len(hand) // 2]
    return card_average(hand) == avg_1_last or card_average(hand) == median

def average_even_is_average_odd(hand):
    return card_average(hand[::2]) == card_average(hand[1::2])

def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] = hand[-1] * 2
    return hand