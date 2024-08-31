def maxEnvelopes(envelopes):
    if not envelopes:
        return 0

    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = [1] * len(envelopes)

    for i in range(len(envelopes)):
        for j in range(i):
            if envelopes[i][1] > envelopes[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# Test cases
envelopes1 = [[5,4],[6,4],[6,7],[2,3]]
print(maxEnvelopes(envelopes1))

envelopes2 = [[1,1],[1,1],[1,1]]
print(maxEnvelopes(envelopes2))
