import unittest


#Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list. 
             Reverse it in-place.
    """
    def reverse(self, head):
        prev = None
        while head is not None:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev



class Tester(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()

    def test_reverse_empty(self):
        empty = self.sol.reverse(None)
        self.assertEquals(empty, None)

    def test_reverse(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        tmp = head
        while tmp is not None:
            print "Item", tmp.val
            tmp = tmp.next
        head_r = self.sol.reverse(head)
        print "Reversed"
        tmp = head_r
        while tmp is not None:
            print "Item", tmp.val
            tmp = tmp.next
        
        
if __name__ == '__main__':
    unittest.main()

