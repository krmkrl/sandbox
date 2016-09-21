class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        # write your code here
        start = 0
        end = len(nums) - 1
        if end < 0:
          return -1
        while start <= end:
          middle = (start + end) / 2
          if target == nums[middle]:
            found = middle
            while target == nums[middle] and middle > 0:
              found = middle
              middle -= 1
            return found
          elif target < nums[middle]:
            end = middle - 1
          else:
            start = middle + 1
        return -1

if __name__ == '__main__':
  sol = Solution()
  index = sol.binarySearch([2,6,8,13,15,17,17,18,19,20], 15)
  print index
  index = sol.binarySearch([4,5,9,9,12,13,14,15,15,18], 10)
  print index
  index = sol.binarySearch([1, 2, 3, 3, 4, 5, 10], 3)
  print index
  index = sol.binarySearch([1,4,4,5,7,7,8,9,9,10], 1)
  print index
  index = sol.binarySearch([1], 1)
  print index
  index = sol.binarySearch([], 1)
  print index
