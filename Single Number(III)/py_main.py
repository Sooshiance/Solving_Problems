class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor_result = 0
    
        for num in nums:
            xor_result ^= num
        
        # Find the rightmost set bit
        rightmost_set_bit = xor_result & -xor_result
        
        num1 = 0
        num2 = 0
        
        for num in nums:
            if num & rightmost_set_bit:
                num1 ^= num
            else:
                num2 ^= num
        
        return [num1, num2]


sol = Solution()


nums = [1, 2, 1, 3, 2, 5]


result = sol.singleNumber(nums)

print(result)
