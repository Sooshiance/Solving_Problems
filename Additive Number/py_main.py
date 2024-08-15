def isAdditiveNumber(num):
    def is_valid(num1, num2, substr):
        if not substr:
            return True
        sum_num = str(int(num1) + int(num2))
        if substr.startswith(sum_num):
            return is_valid(num2, sum_num, substr[len(sum_num):])
        return False

    n = len(num)
    for i in range(1, n // 2 + 1):
        for j in range(i + 1, n):
            num1 = num[:i]
            num2 = num[i:j]
            if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0'):
                continue
            if is_valid(num1, num2, num[j:]):
                return True
    return False


# Test cases
print(isAdditiveNumber("112358"))
print(isAdditiveNumber("199100199"))
