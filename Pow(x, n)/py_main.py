class Solution:
    def powx(self, x, n):
        if n > 0:
            k = 1
            for i in range(n):
                k = k * x 
            return k 

        if n < 0:
            k = 1
            r_n = n * (-1)
            r_x = (1/x)
            for i in range(r_n):
                k = k * r_x
            return k

        if n == 0:
            return 1


sol = Solution()

a = float(input("Enter the x : "))

b = int(input("Enter the n : "))

print(f"x power n is : {sol.powx(a, b)}")
