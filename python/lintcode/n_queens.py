import unittest
import time

class Solution:

    def numBoardToStringBoard(self, num_board):
        str_board = []
        for pos in num_board:
            line = []
            for j in range(0, len(num_board)):
                if j == pos:
                    line.append("Q")
                else:
                    line.append(".")
            str_board.append("".join(line))
        return str_board

    def getCands(self, candidate, row):
        new_cands = []
        #a possible candidate on every column
        for i in range(0, len(candidate)):
            possible_cand = candidate[:] #copy the candidate
            possible_cand[row] = i
            #check clash on every row up to row - 1
            clash = False
            for i in range(0, row):
                if possible_cand[i] == possible_cand[row]:
                    #same column, do not add
                    clash = True
                    break
                if possible_cand[i] == (possible_cand[row] - (row - i)) or possible_cand[i] == (possible_cand[row] + (row - i)): #back up left or back up right
                    #same diagonal, do not add
                    clash = True
                    break
            if clash == False:
                new_cands.append(possible_cand)
        return new_cands

    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        boards = []
        if n <= 0:
            return []

        #create empty nxn board
        num_board = [-1 for i in range(n)]

        #calculate boards
        cands = []
        cands.append(num_board)
        row = 0 #same as index
        while row < n:
            start = time.time()    
            next_cands = []
            for cand in cands:
                next_cands.extend(self.getCands(cand, row))
            cands = next_cands
            row += 1
            end = time.time()
            print "row", row - 1, "took time", (end - start)

        #convert num_board to string board
        for final_board in cands:
            boards.append(self.numBoardToStringBoard(final_board))
        return boards

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
    
    def test_toString(self):
        sb = self.sol.numBoardToStringBoard([0])
        self.assertEquals(sb, ["Q"])    
    
    def test_toString3x3(self):
        sb = self.sol.numBoardToStringBoard([0,2,1]) #note, not a valid n-queens board
        self.assertEquals(sb, ["Q..", "..Q", ".Q."])    
    
    def test_empty(self):
        boards = self.sol.solveNQueens(0)
        self.assertEquals(boards, [])    

    def test_1x1(self):
        boards = self.sol.solveNQueens(1)
        self.assertEquals(boards, [["Q"]])    

    def test_2x2(self):
        boards = self.sol.solveNQueens(2)
        self.assertEquals(boards, [])

    def test_3x3(self):
        boards = self.sol.solveNQueens(3)
        self.assertEquals(boards, [])

    def test_4x4(self):
        boards = self.sol.solveNQueens(4)
        self.assertEquals(boards,
                                [
                                  [".Q..",
                                   "...Q",
                                   "Q...",
                                   "..Q."
                                  ],
                                  ["..Q.",
                                   "Q...",
                                   "...Q",
                                   ".Q.."
                                  ]
                                ])
    def test_10x10(self):
        boards = self.sol.solveNQueens(10)
        self.assertTrue(len(boards) > 0)


if __name__ == '__main__':
    unittest.main()

