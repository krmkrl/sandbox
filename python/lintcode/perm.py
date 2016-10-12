import sys


class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        if len(nums) <= 1:
            return [nums]
        perms = []
        for n in nums:
            rest = [x for x in nums if x != n]
            for sub in self.permute(rest):
                l = [n] + sub
                perms += [l]
        return perms


sol = Solution()
chars = sys.argv[1].split(',')
ints = []
for c in chars:
    ints.append(int(c))
print sol.permute(ints)
