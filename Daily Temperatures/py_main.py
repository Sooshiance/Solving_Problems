def dailyTemperatures(temperatures):
    n = len(temperatures)
    stack = []
    result = [0] * n
    
    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        stack.append(i)
    
    return result

# Test cases
print(dailyTemperatures([73,74,75,71,69,72,76,73]))

print(dailyTemperatures([30,40,50,60]))

print(dailyTemperatures([30,60,90]))
