import unittest

class Solution:

    
    def swap(self, array, i, j):
        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp
        

    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        # you should partition the nums by k
        # and return the partition index as description
        if len(nums) == 0:
            return 0

        start = 0
        end = len(nums) - 1
        while start < end:
            if nums[start] < k:
                start += 1
            else:
                self.swap(nums, start, end)
                end -= 1
        if nums[end] < k:
            end += 1
        return end

class Tester(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()
    
    def test_empty(self):
        k_index = self.sol.partitionArray([], 9)
        self.assertEquals(k_index, 0)    

    def test_k_exist(self):
        k_index = self.sol.partitionArray([3,2,2,1], 2)
        self.assertEquals(k_index, 1)
    
    def test_k_not_exist(self):
        k_index = self.sol.partitionArray([3,2,2,1], 4)
        self.assertEquals(k_index, len([3,2,2,1]))

    def test_k_exist2(self):
        k_index = self.sol.partitionArray([9,9,9,8,9,8,7,9,8,8,8,9,8,9,8,8,6,9], 9)
        self.assertEquals(k_index, 10)
    
    def test_k_not_exist2(self):
        k_index = self.sol.partitionArray([3,2,2,4], 1)
        self.assertEquals(k_index, 0)



if __name__ == '__main__':
    unittest.main()

