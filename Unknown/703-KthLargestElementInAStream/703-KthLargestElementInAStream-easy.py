#
# @lc app=leetcode id=703 lang=python
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """  

        self.minheap = nums
        self.k = k
        # convert the array into a minheap
        heapq.heapify(self.minheap)
        # convert the minheap' length <= k
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        # if the minheap' length <= k, it can still add value
        if len(self.minheap) < self.k:
            heapq.heappush(self.minheap, val)
        # or add the val and pop the top value of minheap if the val >= top value
        elif val > self.minheap[0]:
            heapq.heappushpop(self.minheap, val)
        return self.minheap[0] 


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

