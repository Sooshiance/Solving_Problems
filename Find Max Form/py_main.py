def findMaxForm(strs, m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for s in strs:
        zeros = s.count('0')
        ones = s.count('1')
        
        for i in range(m, zeros - 1, -1):
            for j in range(n, ones - 1, -1):
                dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
    
    return dp[m][n]


# Test cases
strs = ["10","0001","111001","1","0"]
m = 5
n = 3
print(findMaxForm(strs, m, n))


strs = ["10","0","1"]
m = 1
n = 1
print(findMaxForm(strs, m, n))
