import bs
import sys
import unittest

class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        bso = bs.Solution()
        
        l = []
        start = 0
        end = len(matrix) - 1
        if end < 0:
          return False
        while start <= end:
          middle = (start + end) / 2
          if target >= matrix[middle][0] and target <= matrix[middle][len(matrix[middle]) - 1]:
            l = matrix[middle]
            break
          elif target < matrix[middle][0]:
            end = middle - 1
          else: # >
            start = middle + 1

        index = bso.binarySearch(l, target)
        return index != -1


class Test(unittest.TestCase):

  def setUp(self):
    self.sol = Solution()
    self.m = [[1, 3, 5, 7],
         [10, 11, 16, 20],
         [23, 30, 34, 50]]

  def test_3(self):
    self.assertTrue(self.sol.searchMatrix(self.m, 3))
  
  def test_35(self):
    self.assertFalse(self.sol.searchMatrix(self.m, 35))
  
  def test_60(self):
    self.assertFalse(self.sol.searchMatrix(self.m, 60))
  
  def test_22(self):
    self.assertFalse(self.sol.searchMatrix(self.m, 22))

if __name__ == '__main__':
  unittest.main()

