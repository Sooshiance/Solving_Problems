class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        output_list = sorted([num for sublist in lists for num in sublist])

        return output_list


input_list = [[1,4,5],[1,3,4],[2,6]]


sol = Solution()


result = sol.mergeKLists(input_list)

print(result)
