def find132pattern(nums):
    stack = []
    s3 = float('-inf')
    
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] < s3:
            return True
        while stack and nums[i] > stack[-1]:
            s3 = stack.pop()
        stack.append(nums[i])
    
    return False


# Test cases
print(find132pattern([1, 2, 3, 4]))
print(find132pattern([3, 1, 4, 2]))
print(find132pattern([-1, 3, 2, 0]))
