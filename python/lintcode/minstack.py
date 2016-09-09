from collections import deque


class MinStack(object):

    deq = []
    mindeq = []

    def __init__(self):
        # do some intialize if necessary
        self.deq = deque()
        self.mindeq = deque()
        return

    def push(self, number):
        # write yout code here
        self.deq.append(number)
        if len(self.mindeq) > 0:
          self.mindeq.append(min(number, self.mindeq[-1]))
        else:
          self.mindeq.append(number)
        return

    def pop(self):
        # pop and return the top item in stack
        self.mindeq.pop()
        return self.deq.pop()

    def min(self):
        # return the minimum number in stack
        return self.mindeq[-1]

ms = MinStack()
ms.push(3)
ms.push(5)
ms.push(7)
ms.push(2)
ms.push(3)
print ms.pop()
print ms.min()
