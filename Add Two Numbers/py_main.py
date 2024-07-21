class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r_l1 = l1[::-1]
        r_l2 = l2[::-1]
        s1 = ''.join(str(x) for x in r_l1)
        s2 = ''.join(str(y) for y in r_l2)

        n1 = int(s1)
        n2 = int(s2)

        buf = n1 + n2

        l = [int(x) for x in str(buf)]

        res = l[::-1]

        return res


sol = Solution()

ls1 = []

ls2 = []

n = int(input("list length : "))

for i in range(n):
    var = int(input("next number for list 1: "))
    ls1.append(var)

for i in range(n):
    var = int(input("next number for list 1: "))
    ls2.append(var)


final_result = sol.addTwoNumbers(ls1, ls2)


print(final_result)
