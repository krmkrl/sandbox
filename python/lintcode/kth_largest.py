class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
      A_sorted = sorted(A)
      return A_sorted[-k]
