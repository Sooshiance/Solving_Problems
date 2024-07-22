class Solution(object):
    def longestPalindrome(self, s:str):
        """
        :type s: str
        :rtype: str
        """

        if len(s) == 0:
            return ""
        
        longest = ""
        
        for i in range(len(s)):
            # For odd length palindromes
            palindrome1 = self.expand_around_center(s, i, i)
            
            # For even length palindromes
            palindrome2 = self.expand_around_center(s, i, i + 1)
            
            if len(palindrome1) > len(longest):
                longest = palindrome1
            
            if len(palindrome2) > len(longest):
                longest = palindrome2
        
        return longest

    def expand_around_center(self, s:str, left:int, right:int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]


sol = Solution()


x = input("Enter your string : ")

print(f"The longest palindrome of string {x} : ", sol.longestPalindrome(x))
