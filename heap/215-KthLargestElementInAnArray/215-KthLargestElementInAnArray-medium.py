#
# @lc app=leetcode id=215 lang=python
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # create a k'length min heap
        # update the heap when comparing the remaining numbers
        # return the top value of the min heap
        heap = nums[:k]
        heapq.heapify(heap)

        if k == len(nums):
            return heap[0]
        else:
            
            for i in range(k, len(nums)):
                if nums[i] > heap[0]:
                    heapq.heappushpop(heap, nums[i])
            return heap[0]

# @lc code=end

