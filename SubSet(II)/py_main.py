from itertools import chain, combinations


def subsetsWithDup(nums):
    nums.sort()
    res = [[]]
    for i in range(1, len(nums)+1):
        res.extend(list(set(combinations(nums, i))))
    return res


# Test cases
nums1 = [1, 2, 2]
print(subsetsWithDup(nums1))

nums2 = [0]
print(subsetsWithDup(nums2))
