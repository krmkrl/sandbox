import sys

class Solution:
    """
    Ugly number is a number that only have factors 2, 3 and 5.

    Design an algorithm to find the nth ugly number. The first 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12...
    @param {int} n an integer.
    @return {int} the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        uglies = [1]
        i2 = 0
        i3 = 0
        i5 = 0
        while len(uglies) < n:
          n2 = uglies[i2] * 2
          n3 = uglies[i3] * 3
          n5 = uglies[i5] * 5
          min_n = min(n2, n3, n5)
          uglies.append(min_n)
          if n2 == min_n:
            i2 += 1
          if n3 == min_n:
            i3 += 1
          if n5 == min_n:
            i5 += 1
        return uglies[-1]


sol = Solution()
input = int(sys.argv[1])
print sol.nthUglyNumber(input)
