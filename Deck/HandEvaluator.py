from Cards.Card import Card, Rank

# TODO (TASK 3): Implement a function that evaluates a player's poker hand.
#   Loop through all cards in the given 'hand' list and collect their ranks and suits.
#   Use a dictionary to count how many times each rank appears to detect pairs, three of a kind, or four of a kind.
#   Sort these counts from largest to smallest. Use another dictionary to count how many times each suit appears to check
#   for a flush (5 or more cards of the same suit). Remove duplicate ranks and sort them to detect a
#   straight (5 cards in a row). Remember that the Ace (rank 14) can also count as 1 when checking for a straight.
#   If both a straight and a flush occur in the same suit, return "Straight Flush". Otherwise, use the rank counts
#   and flags to determine if the hand is: "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind",
#   "Two Pair", "One Pair", or "High Card". Return a string with the correct hand type at the end.
def evaluate_hand(hand: list[Card]):
    rank_to_value = {
        "2": 2, "3": 3, "4": 4,
        "5": 5, "6": 6, "7": 7,
        "8": 8, "9": 9, "10": 10,
        "J": 11, "Q": 12, "K": 13,
        "A": 14
    }
    ranks = [card.rank for card in hand]
    suits = [card.suit for card in hand]

    rank_count = {}
    for rank in ranks:
        rank_count[rank] = ranks.count(rank)

    suit_count = {}
    for suit in suits:
        suit_count[suit] = suits.count(suit)

    counts = sorted(rank_count.values(), reverse=True)
    is_flush = False
    for suit in suit_count:
        if suit_count[suit] >= 5:
            is_flush = True
            break

    rank_values = sorted(set(rank_to_value[r] for r in ranks))
    is_straight = False
    for index in range(len(rank_values) - 4):
        if rank_values[index + 4] - rank_values[index] == 4:
            is_straight = True
            break

    if set([14, 2, 3, 4, 5]).issubset(set(rank_values)):
        is_straight = True

    if counts == [4, 1]:
        return "Four of a Kind"
    elif counts == [3, 2]:
        return "Full House"
    elif is_flush:
        return "Flush"
    elif is_straight:
        return "Straight"
    elif counts == [3, 1, 1]:
        return "Three of a Kind"
    elif counts == [2, 2, 1]:
        return "Two Pair"
    elif counts == [2, 1, 1, 1]:
        return "One Pair"
    else:
        return "High Card" # If none of the above, it's High Card
