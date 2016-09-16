import sys

class Solution:

    def subset_n(self, S, n):
      if n == 0:
        return [[]]
      if len(S) == n:
        return [S]
      elif len(S) < n:
        return []

      ys = []
      for i in range(0, len(S)):
        subs = self.subset_n(S[i + 1:], n - 1)
        for j in range(0, len(subs)):
          ys.append([S[i]] + subs[j])
      return ys

    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        # write your code here
        S = sorted(S)
        xs = []
        for i in range(0, len(S) + 1):
          xs += self.subset_n(S, i)
        return xs

if __name__ == '__main__':
  sol = Solution()
  l = sys.argv[1].split(',')
  l = map(lambda x: int(x), l)
  print sol.subsets(l)

  print ""
  xs = [1,2,3,4,5]
  n = 5
  print "input", xs, n
  print "result", sol.subset_n(xs, n)
  xs = []
  print "input", xs, n
  print "result", sol.subset_n(xs, n)
  xs = [1,2,3,4,5]
  n = 1
  print "input", xs, n
  print "result", sol.subset_n(xs, n)
  xs = [1,2,3,4,5]
  n = 2
  print "input", xs, n
  print "result", sol.subset_n(xs, n)
  xs = [1,2,3,4,5]
  n = 4
  print "input", xs, n
  print "result", sol.subset_n(xs, n)
