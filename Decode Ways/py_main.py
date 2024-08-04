class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
    
        n = len(s)
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        
        for i in range(2, n + 1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]


sol = Solution()


print(sol.numDecodings("12"))
print(sol.numDecodings("226"))
print(sol.numDecodings("06"))
