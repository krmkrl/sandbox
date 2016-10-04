import unittest


#Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    
  def isInterleaved(self, object1, object2):
    if object1.end >= object2.start:
      return True
    else:
      return False

  def mergeIntervals(self, object1, object2):
    minStart = min(object1.start, object2.start)
    maxEnd = max(object1.end, object2.end)
    return Interval(minStart, maxEnd)

  def insertWithMerge(self, results, interval):
    if self.isInterleaved(results[-1], interval):
      mergedInterval = self.mergeIntervals(results[-1], interval)
      del results[-1]
      results.append(mergedInterval)
    else:
      results.append(interval)


    """
    Insert a new interval into a sorted non-overlapping interval list.
    @param intevals: Sorted non-overlapping interval list
    @param newInterval: The new interval.
    @return: A new sorted non-overlapping interval list with the new interval.
    """
  def insert(self, intervals, newInterval):
    if newInterval is None:
      return intervals
    if len(intervals) == 0:
      return [newInterval]
    
    results = []
    i = 0
    while i < len(intervals):
      if newInterval != None and newInterval.start < intervals[i].start:
        newIntervalCopy = Interval(newInterval.start, newInterval.end)
        newInterval = None
        if len(results) > 0: #has prev
          self.insertWithMerge(results, newIntervalCopy)
        else:
          results.append(newIntervalCopy)
      if len(results) > 0: #has prev
        self.insertWithMerge(results, intervals[i])
      else:
        results.append(intervals[i])
      i = i + 1

    if newInterval != None:
      self.insertWithMerge(results, newInterval)
      
    return results


class Tester(unittest.TestCase):

  def toIntervalObject(self, inter):
    if len(inter) != 2:
      return None
    return Interval(inter[0], inter[1])

  def fromIntervalObject(self, object):
    if object is None:
      return []
    else:
      return [object.start, object.end]

  def setUp(self):
    self.sol = Solution()

  def testMergeIntervals(self):
    interval1 = Interval(3,6)
    interval2 = Interval(5,8)
    mergedInterval = self.sol.mergeIntervals(interval1, interval2)
    self.assertEquals(mergedInterval.start, 3)
    self.assertEquals(mergedInterval.end, 8)

  def testIsInterleaved(self):
    self.assertTrue(self.sol.isInterleaved(Interval(1,3), Interval(2,4)))
  
  def testIsInterleaved2(self):
    self.assertTrue(self.sol.isInterleaved(Interval(2,4), Interval(1,3)))
  
  def testIsInterleaved3(self):
    self.assertTrue(self.sol.isInterleaved(Interval(1,2), Interval(2,5)))
  
  def testIsInterleaved4(self):
    self.assertTrue(self.sol.isInterleaved(Interval(2,5), Interval(1,2)))
  
  def testIsNotInterleaved(self):
    self.assertFalse(self.sol.isInterleaved(Interval(1,3), Interval(5,7)))

  def testInsertWithMerge(self):
    results = map(self.toIntervalObject, [[2,3], [6,8]])
    self.sol.insertWithMerge(results, self.toIntervalObject([7,9]))
    result = map(self.fromIntervalObject, results)
    self.assertEquals(result, [[2,3],[6,9]])

  def test_overlap(self):
    intervals = [[1,2], [5,9]]
    newInterval = [2,5]
    intervalObjects = map(self.toIntervalObject, intervals)
    newIntervalObject = self.toIntervalObject(newInterval)
    newlist = self.sol.insert(intervalObjects, newIntervalObject)
    result = map(self.fromIntervalObject, newlist)
    self.assertEquals(result, [[1,9]])

  def test_non_overlap(self):
    intervals = [[1,2], [5,9]]
    newInterval = [3,4]
    intervalObjects = map(self.toIntervalObject, intervals)
    newIntervalObject = self.toIntervalObject(newInterval)
    newlist = self.sol.insert(intervalObjects, newIntervalObject)
    result = map(self.fromIntervalObject, newlist)
    self.assertEquals(result, [[1,2], [3,4], [5,9]])
  
  def test_insert_first(self):
    intervals = [[4,5], [7,9]]
    newInterval = [2,3]
    intervalObjects = map(self.toIntervalObject, intervals)
    newIntervalObject = self.toIntervalObject(newInterval)
    newlist = self.sol.insert(intervalObjects, newIntervalObject)
    result = map(self.fromIntervalObject, newlist)
    self.assertEquals(result, [[2,3], [4,5], [7,9]])
  
  def test_insert_last(self):
    intervals = [[4,5], [7,9]]
    newInterval = [11,30]
    intervalObjects = map(self.toIntervalObject, intervals)
    newIntervalObject = self.toIntervalObject(newInterval)
    newlist = self.sol.insert(intervalObjects, newIntervalObject)
    result = map(self.fromIntervalObject, newlist)
    self.assertEquals(result, [[4,5], [7,9], [11,30]])

  def test_overlap_first(self):
    intervals = [[4,6], [7,9]]
    newInterval = [2,5]
    intervalObjects = map(self.toIntervalObject, intervals)
    newIntervalObject = self.toIntervalObject(newInterval)
    newlist = self.sol.insert(intervalObjects, newIntervalObject)
    result = map(self.fromIntervalObject, newlist)
    self.assertEquals(result, [[2,6], [7,9]])
  
  def test_overlap_last(self):
    intervals = [[4,5], [7,10]]
    newInterval = [8,12]
    intervalObjects = map(self.toIntervalObject, intervals)
    newIntervalObject = self.toIntervalObject(newInterval)
    newlist = self.sol.insert(intervalObjects, newIntervalObject)
    result = map(self.fromIntervalObject, newlist)
    self.assertEquals(result, [[4,5], [7,12]])
  
  def test_contained(self):
    intervals = [[4,8], [10,12]]
    newInterval = [5,6]
    intervalObjects = map(self.toIntervalObject, intervals)
    newIntervalObject = self.toIntervalObject(newInterval)
    newlist = self.sol.insert(intervalObjects, newIntervalObject)
    result = map(self.fromIntervalObject, newlist)
    self.assertEquals(result, [[4,8], [10,12]])
  
  def test_empty_intervals(self):
    intervals = []
    newInterval = [2,5]
    intervalObjects = map(self.toIntervalObject, intervals)
    newIntervalObject = self.toIntervalObject(newInterval)
    newlist = self.sol.insert(intervalObjects, newIntervalObject)
    result = map(self.fromIntervalObject, newlist)
    self.assertEquals(result, [[2,5]])

  def test_empty_interval(self):
    intervals = [[2,5], [7,8]]
    newInterval = []
    intervalObjects = map(self.toIntervalObject, intervals)
    newIntervalObject = self.toIntervalObject(newInterval)
    newlist = self.sol.insert(intervalObjects, newIntervalObject)
    result = map(self.fromIntervalObject, newlist)
    self.assertEquals(result, [[2,5], [7,8]])

  def test_both_empty(self):
    intervals = []
    newInterval = []
    intervalObjects = map(self.toIntervalObject, intervals)
    newIntervalObject = self.toIntervalObject(newInterval)
    newlist = self.sol.insert(intervalObjects, newIntervalObject)
    self.assertEquals(newlist, [])


if __name__ == '__main__':
  unittest.main()
