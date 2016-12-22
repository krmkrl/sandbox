import unittest

class Solution:

    def getCands(self, candidate, row):
        new_cands = []
        #a possible candidate on every column
        for i in range(0, len(candidate)):
            possible_cand = candidate[:] #copy the candidate
            possible_cand[row] = i
            #check clash on every row up to row - 1
            for i in range(0, row):
                if possible_cand[i] == possible_cand[row]:
                    #same column, do not add
                    break
                if possible_cand[i] == (possible_cand[row] - (row - i)) or possible_cand[i] == (possible_cand[row] + (row - i)): #back up left or back up right
                    #same diagonal, do not add
                    break
            else: #no break statement executed in fo #no break statement executed in forr
                new_cands.append(possible_cand)
        return new_cands

    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """
    def totalNQueens(self, n):
        boards = []
        if n <= 0:
            return 0

        #create empty nxn board
        num_board = [-1 for i in range(n)]

        #calculate boards
        cands = []
        cands.append(num_board)
        row = 0 #same as index
        while row < n:
            next_cands = []
            for cand in cands:
                next_cands.extend(self.getCands(cand, row))
            cands = next_cands
            row += 1
        return len(cands)

class Tester(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()

    def test_getCands1x1(self):
        cands = self.sol.getCands([-1], 0)
        self.assertEquals(cands, [[0]])
    
    def test_getCands2x2(self):
        cands = self.sol.getCands([0,-1], 1)
        self.assertEquals(cands, [])
    
    def test_getCands3x3(self):
        cands = self.sol.getCands([0,-1,-1], 1)
        self.assertEquals(cands, [[0,2,-1]])
    
    def test_getCands3x3_l(self):
        cands = self.sol.getCands([0,2,-1], 2)
        self.assertEquals(cands, [])
    
    def test_empty(self):
        boards = self.sol.totalNQueens(0)
        self.assertEquals(boards, 0)    

    def test_1x1(self):
        boards = self.sol.totalNQueens(1)
        self.assertEquals(boards, 1)    

    def test_2x2(self):
        boards = self.sol.totalNQueens(2)
        self.assertEquals(boards, 0)

    def test_3x3(self):
        boards = self.sol.totalNQueens(3)
        self.assertEquals(boards, 0)

    def test_4x4(self):
        boards = self.sol.totalNQueens(4)
        self.assertEquals(boards, 2)
    
    def test_10x10(self):
        boards = self.sol.totalNQueens(10)
        self.assertEquals(boards, 724)


if __name__ == '__main__':
    unittest.main()

