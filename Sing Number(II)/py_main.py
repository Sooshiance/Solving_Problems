def singleNumber(nums):
    ones = 0
    twos = 0
    
    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones
        
    return ones


# Test the function with the given examples
print(singleNumber([2,2,3,2]))  # Output: 3
print(singleNumber([0,1,0,1,0,1,99]))  # Output: 99
