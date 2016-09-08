import sys

class Solution:
    # @param s: a list of char
    # @param offset: an integer 
    # @return: nothing
    def rotateString(self, s, offset):
      # write you code here
      #s = s[-offset:] + s[:-offset]

sol = Solution()
inputStr = sys.argv[1]
sol.rotateString(inputStr, int(sys.argv[2]))
print inputStr
