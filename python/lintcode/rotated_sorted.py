import unittest

class Solution:

    """
    @param nums: The rotated sorted array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        #find where the array is rotated
        split = len(nums)
        for index, item in enumerate(nums):
            if item < nums[index - 1]:
                split = index
        #rotate back into sorted state
        for i in range(len(nums) - split):
            tmp = nums.pop()
            nums.insert(0, tmp)



class Tester(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()

    def test_empty(self):
        nums = []
        self.sol.recoverRotatedSortedArray(nums)
        self.assertEquals(nums, [])
    
    def test_one(self):
        nums = [1]
        self.sol.recoverRotatedSortedArray(nums)
        self.assertEquals(nums, [1])

    def test_45123(self):
        nums = [4,5,1,2,3]
        self.sol.recoverRotatedSortedArray(nums)
        self.assertEquals(nums, [1,2,3,4,5])
    
    def test_34512(self):
        nums = [3,4,5,1,2]
        self.sol.recoverRotatedSortedArray(nums)
        self.assertEquals(nums, [1,2,3,4,5])
    
    def test_sorted(self):
        nums = [1,2,3,4]
        self.sol.recoverRotatedSortedArray(nums)
        self.assertEquals(nums, [1,2,3,4])
    
    
if __name__ == '__main__':
    unittest.main()

