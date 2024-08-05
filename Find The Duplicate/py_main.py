class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


sol = Solution()

print(sol.findDuplicate([1, 3, 4, 2, 2]))
