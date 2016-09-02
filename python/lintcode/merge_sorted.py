class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        # write your code here
        merged = []
        i = 0
        j = 0
        while i < len(A) and j < len(B):
          if A[i] < B[j]:
            merged.append(A[i])
            i += 1
          else:
            merged.append(B[j])
            j += 1

        # copy rest, one or both lists are now empty
        while i < len(A):
          merged.append(A[i])
          i += 1
        while j < len(B):
          merged.append(B[j])
          j += 1

        return merged

sol = Solution()
A = [1,2,3,4,5,8,9,23]
B = [3,6,9,10,22]

print sol.mergeSortedArray(A, B)
