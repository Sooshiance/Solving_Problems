def count_distinct_partitions(nums, k):
    MOD = 109 + 7
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(k, -1, -1):
            dp[i][j] = (2 * dp[i - 1][j]) % MOD
            if j - nums[i - 1] - 1 >= 0:
                dp[i][j] -= dp[i - 1][j - nums[i - 1] - 1]
            dp[i][j] %= MOD

    return (dp[n][k] - 1) % MOD


# Test cases
nums = [6,6]
k = 2
print(count_distinct_partitions(nums, k))
