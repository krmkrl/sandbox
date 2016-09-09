class Solution:
    def strStr(self, source, target):
        # write your code here
        if source is not None and target is not None:
            s = 0
            while s <= len(source):
              if target == source[s:s + len(target)]:
                return s
              s += 1
        return -1

sol = Solution()
print sol.strStr("ababaabaaaa", "abaa") == 2
print sol.strStr("abcabcabcdabc", "abcd") == 6
print sol.strStr("abcdabcdefg", "bcd") == 1
print sol.strStr("abc", "efgabc") == -1
print sol.strStr("efgabc", "efgabc") == 0
print sol.strStr("", "efgabc") == -1
print sol.strStr("abc", "") == 0
print sol.strStr("", "") == 0
print sol.strStr(None, "xdf") == -1
print sol.strStr(None, "") == -1
print sol.strStr(None, None) == -1
print sol.strStr("", None) == -1
print sol.strStr("abc", None) == -1
