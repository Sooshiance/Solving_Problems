from itertools import combinations


def subsets(nums):
    res = []
    for i in range(len(nums) + 1):
        res += [list(comb) for comb in combinations(nums, i)]
    return res


print(subsets([1, 2, 3]))
print(subsets([0]))
