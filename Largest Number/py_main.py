from functools import cmp_to_key


class Solution(object):
    def largestNumber(self, nums:list) -> str :
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(lambda a, b: int(b + a) - int(a + b)))
        return str(int(''.join(nums)))


sol = Solution()


# Example
nums = [9, 3, 30, 34, 5, 9]

result = sol.largestNumber(nums)

print(result)
