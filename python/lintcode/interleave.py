import unittest

class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        if len(s1) + len(s2) != len(s3):
          return False

        i1 = 0
        i2 = 0
        i = 0
        while i < len(s3):
          ch = s3[i]
          if i1 < len(s1) and i2 < len(s2) and s1[i1] == ch and s2[i2] == ch:
            #find which one to step
            t1 = i1 + 1
            t2 = i2 + 1
            ti = i + 1
            while ti < len(s3):
              tch = s3[ti]
              if t1 < len(s1) and t2 < len(s2) and s1[t1] == tch and s2[t2] == tch:
                t1 += 1
                t2 += 1
              elif t1 < len(s1) and s1[t1] == tch:
                i1 += 1
                break
              elif t2 < len(s2) and s2[t2] == tch:
                i2 += 1
                break
              ti += 1
            if ti == len(s3):
              #pick one (i1)
              i1 += 1
          elif i1 < len(s1) and s1[i1] == ch:
            i1 += 1
          elif i2 < len(s2) and s2[i2] == ch:
            i2 += 1
          else:
            return False
          i += 1

        return True


class InterleaveTest(unittest.TestCase):

  def setUp(self):
    self.sol = Solution()

  def test_empty_input(self):
    self.assertFalse(self.sol.isInterleave("", "", "1"))
  
  def test_empty_input_s3(self):
    self.assertTrue(self.sol.isInterleave("", "", ""))
  
  def test_empty_s1(self):
    self.assertFalse(self.sol.isInterleave("", "dbbca", "aadbbcbcac"))
  
  def test_empty_s2(self):
    self.assertFalse(self.sol.isInterleave("aabcc", "", "aadbbcbcac"))
  
  def test_empty_s3(self):
    self.assertFalse(self.sol.isInterleave("aabcc", "dbbca", ""))
  
  def test_non_empty_true(self):
    self.assertTrue(self.sol.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
 
  def test_non_empty_false(self):
    self.assertFalse(self.sol.isInterleave("aabcc", "dbbca", "aadbbbaccc"))
  
  def test_equal_strings(self):
    self.assertFalse(self.sol.isInterleave("abcdef", "abcdef", "abcdef"))

  def test_equal_strings(self):
    self.assertTrue(self.sol.isInterleave("abcdef", "abcdef", "abcdefabcdef"))

  def test_equal_strings_every_other(self):
    self.assertTrue(self.sol.isInterleave("abcdef", "abcdef", "aabbccddeeff"))

  def test_different_strings_every_other(self):
    self.assertTrue(self.sol.isInterleave("abcdef", "axkl", "axabcdklef"))

  def test_different_strings_first_same(self):
    self.assertTrue(self.sol.isInterleave("abc", "akl", "aakblc"))

  def test_different_strings_first_same_2(self):
    self.assertTrue(self.sol.isInterleave("abc", "akl", "abaklc"))

  def test_different_strings_first_same_fail(self):
    self.assertFalse(self.sol.isInterleave("abc", "akl", "aaklcb"))

  def test_same_strings_same_chars(self):
    self.assertTrue(self.sol.isInterleave("aaaaa", "aa", "aaaaaaa"))
  
  def test_same_strings_same_chars_2(self):
    self.assertTrue(self.sol.isInterleave("aa", "aaaaa", "aaaaaaa"))


if __name__ == '__main__':
  unittest.main()
