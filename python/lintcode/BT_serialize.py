"""
Definition of TreeNode:
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:

    def recurseDFS(self, node):
        if node is None:
          return "#"
        else:
          return str(node.val) + "," + self.recurseDFS(node.left) + "," + self.recurseDFS(node.right)

    def deRecurseDFS(self, data):
        if len(data) > 0:
          val = data.pop(0) #get and remove first item in list
          if val == '#':
            return None
          else:
            node = TreeNode(int(val))
            node.left = self.deRecurseDFS(data)
            node.right = self.deRecurseDFS(data)
          return node
        else:
          return None

    def encodeBFS(self, node):
      nodes = []
      nodes.append(node)
      encodeStr = ''
      while len(nodes) > 0:
        node = nodes.pop(0)
        if node is None:
          encodeStr += '#'
        else:
          encodeStr += str(node.val)
          nodes.append(node.left)
          nodes.append(node.right)
        encodeStr += ','
      return encodeStr[:-1] #skip trailing comma

    def decodeBFS(self, data):
      root = TreeNode(int(data[0]))
      parents = []
      parents.append(root)
      child = 1
      while len(parents) > 0:
        parent = parents.pop(0)
        if child >= len(data) or data[child] == '#':
          parent.left = None
        else:
          parent.left = TreeNode(int(data[child]))
          parents.append(parent.left)
        child += 1
        if child >= len(data) or data[child] == '#':
          parent.right = None
        else:
          parent.right = TreeNode(int(data[child]))
          parents.append(parent.right)
        child += 1

      return root

    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self, root):
        # write your code here
        return self.encodeBFS(root)

    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    '''
    def deserialize(self, data):
        # write your code here
        if data[0] == '#':
          return None
        return self.decodeBFS(data.split(","))


if __name__ == "__main__":
  sol = Solution()

  tree = TreeNode(3)
  tree.left = TreeNode(9)
  tree.right = TreeNode(20)
  tree.right.left = TreeNode(15)
  tree.right.right = TreeNode(7)

  serStr = sol.serialize(tree)
  print serStr
  desTree = sol.deserialize(serStr)
  #serialize result to check correctness
  ser2Str = sol.serialize(desTree)

  tree = None
  empty = sol.serialize(tree)
  sol.deserialize(empty)

  print ser2Str
