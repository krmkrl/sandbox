import unittest

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def move1To2(self):
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())

    def push(self, element):
        self.stack1.append(element)

    def top(self):
        # return the top element
        if not self.stack2:
            self.move1To2()
        if not self.stack2:
            return None
        return self.stack2[-1]

    def pop(self):
        # pop and return the top element
        if not self.stack2:
            self.move1To2()
        if not self.stack2:
            return None
        return self.stack2.pop()

class Tester(unittest.TestCase):
    
    def setUp(self):
        self.q = MyQueue()

    def test_empty(self):
        nums = []
        t = self.q.top()
        self.assertEquals(t, None)
    
    def test_one(self):
        self.q.push(1)
	self.q.push(2)
	p = self.q.pop()
        self.assertEquals(p, 1)
	t = self.q.top()
	self.assertEquals(t, 2)
	p = self.q.pop()
	self.assertEquals(p, 2)
	t = self.q.pop()
	self.assertEquals(t, None)

    
if __name__ == '__main__':
    unittest.main()

