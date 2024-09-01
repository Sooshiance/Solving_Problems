def maximumSwap(num):
    num = list(str(num))
    last_occurrence = {int(val): i for i, val in enumerate(num)}

    for i, val in enumerate(num):
        for d in range(9, int(val), -1):
            if d in last_occurrence and last_occurrence[d] > i:
                num[i], num[last_occurrence[d]] = num[last_occurrence[d]], num[i]
                return int("".join(num))

    return int("".join(num))


# Test cases
print(maximumSwap(2736))
print(maximumSwap(9973))
