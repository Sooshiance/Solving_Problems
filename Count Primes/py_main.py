def count_primes(n):
    if n < 2:
        return 0
    else:
        cp = []
        for i in range(2, n + 1):
            k = 0
            for j in range(2, i+1):
                if i % j == 0:
                    k += 1
            if k < 2:
                cp.append(i)
        return len(cp)


# Test cases
print(count_primes(10))
print(count_primes(0))
print(count_primes(1))
