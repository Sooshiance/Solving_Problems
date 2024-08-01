class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        k = n / 4

        l = int(k)
        
        x = None

        for i in range(l+1):
            if n == i ** 4:
                print(i)
                x = i
            else:
                continue
        
        if x is not None:
            return True
        else:
            return False


sol = Solution()

n = int(input("Enter a number : "))


b = sol.isPowerOfFour(n)

if b == True:
    print("Yes")
else:
    print("No")
