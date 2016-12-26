import unittest


#Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:

    """
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    def reverseBetween(self, head, m, n):
        i = 1
        prev = None
        start = head
        rev_last = head
        rev_prev = prev
        while head is not None:
            tmp = head.next
            if i == m:
                rev_last = head
                rev_prev = prev
            if i >= m and i <= n:
                head.next = prev
            if i == n:
                rev_last.next = tmp
                if rev_prev is not None:
                    rev_prev.next = head
                if m == 1:
                    start = head
            prev = head
            head = tmp
            i += 1
        return start



class Tester(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()

    def test_reverse_empty(self):
        empty = self.sol.reverseBetween(None, 2, 4)
        self.assertEquals(empty, None)

    def test_reverse_1_1(self):
        head = ListNode(1)
        head_r = self.sol.reverseBetween(head, 1, 1)
        self.assertEquals(1, head_r.val)
        self.assertEquals(None, head_r.next)

    def test_reverse_2_4(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        print "List 2_4"
        tmp = head
        while tmp is not None:
            print "Item", tmp.val
            tmp = tmp.next
        head_r = self.sol.reverseBetween(head, 2, 4)
        print "Reversed_2_4"
        tmp = head_r
        while tmp is not None:
            print "Item", tmp.val
            tmp = tmp.next
    
    def test_reverse_1_3(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        print "List 1_3"
        tmp = head
        while tmp is not None:
            print "Item", tmp.val
            tmp = tmp.next
        head_r = self.sol.reverseBetween(head, 1, 3)
        print "Reversed_1_3"
        tmp = head_r
        while tmp is not None:
            print "Item", tmp.val
            tmp = tmp.next
    
    def test_reverse_1_5(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        print "List 1_5"
        tmp = head
        while tmp is not None:
            print "Item", tmp.val
            tmp = tmp.next
        head_r = self.sol.reverseBetween(head, 1, 5)
        print "Reversed_1_5"
        tmp = head_r
        while tmp is not None:
            print "Item", tmp.val
            tmp = tmp.next
        
        
        
if __name__ == '__main__':
    unittest.main()

