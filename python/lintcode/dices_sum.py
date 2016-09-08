import sys

sides = 6

def getsum(sums, index):
  val = 0
  for i in range(index - sides, index):
    if i in sums:
      val += sums[i]
  return val


class Solution:
    # @param {int} n an integer
    # @return {tuple[]} a list of tuple(sum, probability)
    def dicesSum(self, n):
        # Write your code here
        sums = {}
        for i in range(1, sides + 1):
          sums[i] = 1

        for dice in range(2, n + 1):
          newsums = {} 
          for j in range(1, dice * sides + 1):
            jsum = getsum(sums, j)
            newsums[j] = jsum
          sums = newsums
        
        probs = []
        for k,v in sums.items():
          if k >= n:
            probs.append([k, v / float(sides**n)])
          
        return probs


sol = Solution()
print sol.dicesSum(int(sys.argv[1]))
