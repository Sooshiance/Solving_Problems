def removeInvalidParentheses(s):
    def is_valid(s):
        cnt = 0
        for char in s:
            if char == '(':
                cnt += 1
            elif char == ')':
                cnt -= 1
                if cnt < 0:
                    return False
        return cnt == 0

    level = {s}
    while True:
        valid = list(filter(is_valid, level))
        if valid:
            return valid
        level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}


s1 = "()())()"
s2 = "(a)())()"
print(removeInvalidParentheses(s1))
print(removeInvalidParentheses(s2))
