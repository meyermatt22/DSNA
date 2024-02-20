def last_stone(stones):
    # Write your code here
    if len(stones) == 1:
        return stones[0]

    if len(stones) < 1:
        return 0

    sortedStones = sorted(stones)

    largest = sortedStones[-1]
    largest2 = sortedStones[-2]
    smashRes = largest - largest2

    del sortedStones[-2:]
    if smashRes:
        sortedStones.append(smashRes)

    return last_stone(sortedStones)
