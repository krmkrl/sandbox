import sys


class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        if not isinstance(nestedList, list):
          return [nestedList]
        xs = []
        for elem in nestedList:
          if isinstance(elem, list):
            xs += self.flatten(elem)
          else:
            xs.append(elem)
        return xs

sol = Solution()
l = [1,2,[1,2]]
print "input",l, "result",sol.flatten(l)
l = [4,[3,[2,[1]]]]
print "input",l, "result",sol.flatten(l)
l = 10
print "input",l, "result",sol.flatten(l)
