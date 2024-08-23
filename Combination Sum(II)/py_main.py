def combinationSum2(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            res.append(path)
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            backtrack(i + 1, target - candidates[i], path + [candidates[i]])

    candidates.sort()
    res = []
    backtrack(0, target, [])
    return res


# Test cases

candidates1 = [10, 1, 2, 7, 6, 1, 5]
target1 = 8
print(combinationSum2(candidates1, target1))

candidates2 = [2, 5, 2, 1, 2]
target2 = 5
print(combinationSum2(candidates2, target2))
