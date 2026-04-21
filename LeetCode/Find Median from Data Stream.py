import heapq
class MedianFinder(object):
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
    def addNum(self, num):
        heapq.heappush(self.max_heap,-num)
        num = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap,num)
        if len(self.min_heap) > len(self.max_heap):
            el = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,-el)
    def findMedian(self):
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + -self.max_heap[0]) / 2
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return -self.max_heap[0]

