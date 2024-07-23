class Solution(object):
    def reverse(self, num):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if num < 0 else 1
        num = abs(num)
        reverse = 0
        
        while num != 0:
            digit = num % 10
            reverse = reverse * 10 + digit
            num //= 10
        
        return sign * reverse


sol = Solution()


x = int(input("Enter choosen Number : "))


print(f"Reverse of Integer {x} is : {sol.reverse(x)}")
