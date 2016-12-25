import unittest
import time

class LFUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {} #map key to value
        self.usage = {} #map of key to (usage, timestamp)


    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.capacity == 0:
            return
        if len(self.map) == self.capacity and key not in self.map:
            #remove key with the lowest usage
            k_u_list = self.usage.items()
            min_key, (min_usage, ts_min) = k_u_list[0]
            for k,(usage, ts) in k_u_list:
                if usage < min_usage or (usage == min_usage and ts < ts_min):
                    min_key = k
                    min_usage = usage
                    ts_min = ts 
            del self.map[min_key]
            del self.usage[min_key]
        self.map[key] = value
        now = time.time()
        if key in self.usage:
            (usage, ts) = self.usage[key]
            self.usage[key] = (usage + 1, now)
        else:
            self.usage[key] = (1, now)


    # @return an integer
    def get(self, key):
        if key in self.map:
            val = self.map[key]
            (usage, _) = self.usage[key]
            self.usage[key] = (usage + 1, time.time())
            return val
        else:
            return -1

class Tester(unittest.TestCase):
    
    def test_capa_0(self):
        lfu = LFUCache(0)
        self.assertEquals(lfu.get(3), -1)
        lfu.set(2,2)
        self.assertEquals(lfu.get(2), -1)
    
    def test_capa_1(self):
        lfu = LFUCache(1)
        self.assertEquals(lfu.get(2), -1)
        lfu.set(2,2)
        self.assertEquals(lfu.get(2), 2)
        lfu.set(2,1)
        self.assertEquals(lfu.get(2), 1)
        lfu.set(1,4)
        self.assertEquals(lfu.get(1), 4)
        self.assertEquals(lfu.get(2), -1)

    def test_capa_3(self):
        lfu = LFUCache(3)
        lfu.set(2,2)
        lfu.set(1,1)
        self.assertEquals(lfu.get(2), 2)
        self.assertEquals(lfu.get(1), 1)
        self.assertEquals(lfu.get(2), 2)
        lfu.set(3,3)
        lfu.set(4,4)
        self.assertEquals(lfu.get(3), -1)
        self.assertEquals(lfu.get(2), 2)
        self.assertEquals(lfu.get(1), 1)
        self.assertEquals(lfu.get(4), 4)

    def test_capa_3_2(self):
        lfu = LFUCache(3)
        lfu.set(1,10)
        lfu.set(2,20)
        lfu.set(3,30)
        self.assertEquals(lfu.get(1), 10)
        lfu.set(4,40)
        self.assertEquals(lfu.get(4), 40)
        self.assertEquals(lfu.get(3), 30)
        self.assertEquals(lfu.get(2), -1)
        self.assertEquals(lfu.get(1), 10)
        lfu.set(5,50)
        self.assertEquals(lfu.get(1), 10)
        self.assertEquals(lfu.get(2), -1)
        self.assertEquals(lfu.get(3), 30)
        self.assertEquals(lfu.get(4), -1)
        self.assertEquals(lfu.get(5), 50)

    def test_many(self):
        lfu = LFUCache(2048)
        num_sets = 4000
        num_get = 8000
        start = time.time()
        for i in range(num_sets):
            lfu.set(i, i*10)
        end = time.time()
        print "set time", (end - start)
         
        start = time.time()
        for i in range(num_sets):
            lfu.get(i)
            lfu.get(i * 400) # miss
        end = time.time()
        print "get time", (end - start)


if __name__ == '__main__':
    unittest.main()

