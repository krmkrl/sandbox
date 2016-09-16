import sys
import subsets

class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        # write your code here
        s = subsets.Solution()
        xs = s.subsets(S)
        unique = []
        for i in range(0, len(xs)):
            if xs[i] not in xs[i + 1:]:
                unique.append(xs[i])
        return unique


sol = Solution()
l = sys.argv[1].split(',')
l = map(lambda x: int(x), l)
print sol.subsetsWithDup(l)

