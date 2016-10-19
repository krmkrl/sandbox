import unittest

class Solution:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window
             Return "" if there is no such a string
    """
    def minWindow(self, source, target):
        tlen = len(target)
        for searchLength in range(tlen, len(source) + 1):
            for pos in range(0, len(source) - searchLength + 1):
                substr = source[pos:(pos + searchLength)]
                used = set() #used indices of substr
                for c in target:
                    for s in range(0, len(substr)):
                        if c == substr[s] and not s in used:
                            used.add(s) #index s used
                            break
                if len(used) == tlen:
                    return substr
        return ""
            
        

class Tester(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()
    
    def test_empty(self):
        window = self.sol.minWindow("", "ab")
        self.assertEquals(window, "")    

    def test_banc(self):
        window = self.sol.minWindow("ADOBECODEBANC", "ABC")
        self.assertEquals(window, "BANC")
    
    def test_cde(self):
        window = self.sol.minWindow("ADOBECODEBANC", "ECD")
        self.assertEquals(window, "ECOD")
    
    def test_none(self):
        window = self.sol.minWindow("ADOBECODEBANC", "YBXD")
        self.assertEquals(window, "")
    
    def test_target_none(self):
        window = self.sol.minWindow("ADOBECODEBANC", "")
        self.assertEquals(window, "")

    def test_acc(self):
        window = self.sol.minWindow("abcdecf", "acc")
        self.assertEquals(window, "abcdec")

    def test_all(self):
        window = self.sol.minWindow("ADOBECODEBANC", "ADOBECODEBANC")
        self.assertEquals(window, "ADOBECODEBANC")



if __name__ == '__main__':
    unittest.main()

