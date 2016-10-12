import sys

class Solution:

    def dup(self, nums):
        unique = []
        for i in range(0, len(nums)):
            if nums[i] not in nums[i + 1:]:
                unique.append(nums[i])
        return unique


    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permuteUniques(self, nums):
        # write your code here
        if len(nums) <= 1:
            return [nums]
        perms = []
        for n in range(0, len(nums)):
            rest = []
            i = 0
            for x in nums:
                if i != n:
                    rest.append(x)
                i += 1
            for sub in self.permuteUnique(rest):
                l = [nums[n]] + sub
                perms += [l] 
        return perms

    def permuteUnique(self, nums):
        return self.dup(self.permuteUniques(nums))


sol = Solution()
chars = sys.argv[1].split(',')
ints = []
for c in chars:
    ints.append(int(c))
testdups = sol.dup(ints)
print testdups
alls = sol.permuteUnique(ints)
unique = sol.dup(alls)
print unique
