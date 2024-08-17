def maximumGap(nums):
    if len(nums) < 2:
        return 0
    
    nums.sort()
    max_diff = 0
    for i in range(1, len(nums)):
        max_diff = max(max_diff, nums[i] - nums[i-1])
    
    return max_diff


# Test cases
print(maximumGap([3,6,9,1]))
print(maximumGap([10]))
