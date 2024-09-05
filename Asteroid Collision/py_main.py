def asteroidCollision(asteroids):
    stack = []
    
    for asteroid in asteroids:
        while stack and asteroid < 0 < stack[-1]:
            if stack[-1] < -asteroid:
                stack.pop()
                continue
            elif stack[-1] == -asteroid:
                stack.pop()
            break
        else:
            stack.append(asteroid)
    
    return stack


# Test cases
print(asteroidCollision([5, 10, -5]))
print(asteroidCollision([8, -8]))
print(asteroidCollision([10, 2, -5]))
