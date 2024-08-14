def divide(dividend, divisor):
    if dividend == 0:
        return 0
    
    negative = (dividend < 0) != (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    
    quotient = 0
    while dividend >= divisor:
        temp, i = divisor, 1
        while dividend >= temp:
            dividend -= temp
            quotient += i
            i <<= 1
            temp <<= 1
    
    if negative:
        quotient = -quotient
    
    return max(min(quotient, 231 - 1), -231)


# Test cases
print(divide(10, 3)) # Output: 3
print(divide(7, -3)) # Output: -2
