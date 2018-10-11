import sys

sides = 6

def getsum(sums, index):
  val = 0
  for i in range(index - sides, index):
    if i > 0 and i in sums:
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
          for j in range(dice, dice * sides + 1):
            jsum = getsum(sums, j)
            newsums[j] = jsum
          sums = newsums
        
        probs = []
        amount = float(sides**n)
        for k,v in sums.items():
          probs.append([k, v / amount])
          
        return probs


sol = Solution()
print sol.dicesSum(int(sys.argv[1]))
