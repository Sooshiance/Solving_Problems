from collections import defaultdict


def findTargetSumWays(nums, target):
    count = defaultdict(int)
    count[0] = 1
    
    for num in nums:
        new_count = defaultdict(int)
        for old_sum, freq in count.items():
            new_count[old_sum + num] += freq
            new_count[old_sum - num] += freq
        count = new_count
    
    return count[target]


# Test cases
print(findTargetSumWays([1, 1, 1, 1, 1], 3))
print(findTargetSumWays([1], 1))
