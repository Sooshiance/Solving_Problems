def best_poker_hand(ranks, suits):
    if len(set(suits)) == 1:
        return "Flush"
    elif len(set(ranks)) == 2:
        return "Three of a Kind"
    elif len(set(ranks)) == 3:
        return "Pair"
    else:
        return "High Card"


# Test cases
print(best_poker_hand([13,2,3,1,9], ['a','a','a','a','a']))
print(best_poker_hand([4,4,2,4,4], ['d','a','a','b','c']))
print(best_poker_hand([10,10,2,12,9], ['a','b','c','a','d']))
