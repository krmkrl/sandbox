import sys
import BT_serialize


def findInorder(node, k1, k2, matches):
  if not node:
    return
  if node.left:
    findInorder(node.left, k1, k2, matches)
  if node.val >= k1 and node.val <= k2:
    matches.append(node.val)
  if node.right:
    findInorder(node.right, k1, k2, matches)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:

    """
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """    
    def searchRange(self, root, k1, k2):
        # write your code here
        if k2 < k1:
          return []
        
        #inorder traversal of BT to get the values in asc. order
        matches = []
        findInorder(root, k1, k2, matches)
        return matches



bt = BT_serialize.Solution()
l = sys.argv[1]
tree = bt.decodeBFS(l.split(","))

k1 = int(sys.argv[2])
k2 = int(sys.argv[3])

sol = Solution()
print sol.searchRange(tree, k1, k2)
