def removeKDigits(num, k):
    stack = []

    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    # Handle the case where k is still greater than 0
    while k > 0:
        stack.pop()
        k -= 1

    # Remove leading zeros
    return "".join(stack).lstrip('0') or "0"


# Test cases
print(removeKDigits("1432219", 3))
print(removeKDigits("10200", 1))
print(removeKDigits("10", 2))
