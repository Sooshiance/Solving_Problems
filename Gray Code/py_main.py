def grayCode(n):
    result = [0]
    for i in range(1, 2*n):
        result.append(i ^ (i >> 1))
    return result


# Test Cases
n = 2
print(grayCode(n))

n = 1
print(grayCode(n))
