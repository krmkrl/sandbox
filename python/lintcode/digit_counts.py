import sys

class Solution:
    # @param k & n  two integer
    # @return ans a integer
    def digitCounts(self, k, n):
        num = 0
        for i in range(0, n + 1):
            for ch in str(i):
                if ch == str(k):
                    num += 1
        return num

sol = Solution()
print sol.digitCounts(int(sys.argv[1]), int(sys.argv[2]))
