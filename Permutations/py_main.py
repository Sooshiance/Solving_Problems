class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(self.calculate_permutations(nums))
    
    def calculate_permutations(self, iterable, r=None):
        # TODO: Remove duplicate elements
        pool = tuple(iterable)
        n = len(pool)

        # TODO: Number of Rotations in Permutation
        r = n if r is None else r

        # TODO: based on formula of permutation ((n!)/(n-r)!) s.t (n>=r)
        if r > n:
            return

        # TODO: make a list from 0 to n-1
        indices = list(range(n))

        # TODO: based on formula of permutation ((n!)/(n-r)!) we need (n)! and (n-r)!
        cycles = list(range(n, n-r, -1))

        # TODO: current value for pool[i]
        yield tuple(pool[i] for i in indices[:r])

        while n:
            # TODO: Do Permutation
            for i in reversed(range(r)):
                cycles[i] -= 1
                if cycles[i] == 0:
                    indices[i:] = indices[i+1:] + indices[i:i+1]
                    cycles[i] = n - i
                else:
                    j = cycles[i]
                    indices[i], indices[-j] = indices[-j], indices[i]
                    yield tuple(pool[i] for i in indices[:r])
                    break
            else:
                return


sol = Solution()


l = [1, 2, 3]


print(sol.permute(l))
