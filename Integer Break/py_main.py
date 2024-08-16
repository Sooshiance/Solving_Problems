def maxProduct(n):
    if n == 2:
        return 1
    if n == 3:
        return 2
    if n % 3 == 0:
        return 3  (n // 3)
    elif n % 3 == 1:
        return 3  ((n // 3) - 1) * 4
    else:
        return 3  (n // 3) * 2


# Test cases
print(maxProduct(2))
print(maxProduct(10))
