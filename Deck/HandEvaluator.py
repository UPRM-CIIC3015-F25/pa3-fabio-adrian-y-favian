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
    ranks = [card.rank for card in hand]
    suits = [card.suit for card in hand]

    rank_count = {}
    for r in ranks:
        rank_count[r] = rank_count.get(r, 0) + 1

    counts = sorted(rank_count.values(), reverse=True)

    suit_count = {}
    for s in suits:
        suit_count[s] = suit_count.get(s, 0) + 1

    is_flush = any(count >= 5 for count in suit_count.values())

    values = sorted({r.value for r in ranks})

    is_straight = False

    for i in range(len(values) - 4):
        if values[i+4] - values[i] == 4 and \
           values[i+1] == values[i] + 1 and \
           values[i+2] == values[i] + 2 and \
           values[i+3] == values[i] + 3:
            is_straight = True
    if {14, 2, 3, 4, 5}.issubset(values):
        is_straight = True

    if counts == [4, 1] or counts == [4]:
        return "Four of a Kind"
    if counts == [3, 2]:
        return "Full House"
    if is_flush:
        return "Flush"
    if is_straight:
        return "Straight"
    if counts == [3, 1, 1] or counts == [3, 1]:
        return "Three of a Kind"
    if counts == [2, 2, 1] or counts == [2, 2]:
        return "Two Pair"
    if counts == [2, 1, 1, 1] or counts == [2, 1]:
        return "One Pair"
    return "High Card"
