def arrayNesting(nums):
    visited = [False] * len(nums)
    max_length = 0

    for i in range(len(nums)):
        if not visited[i]:
            start = nums[i]
            count = 0
            while not visited[start]:
                visited[start] = True
                count += 1
                start = nums[start]
            max_length = max(max_length, count)

    return max_length


# Test cases
nums1 = [5, 4, 0, 3, 1, 6, 2]
print(arrayNesting(nums1))

nums2 = [0, 1, 2]
print(arrayNesting(nums2))
