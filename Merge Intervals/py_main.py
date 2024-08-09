class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        merged = []
        
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged


sol = Solution()


# Example 1
intervals1 = [[1,3],[2,6],[8,10],[15,18]]
print(sol.merge_intervals(intervals1))

# Example 2
intervals2 = [[1,4],[4,5]]
print(sol.merge_intervals(intervals2))
