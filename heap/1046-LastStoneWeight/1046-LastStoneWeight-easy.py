#
# @lc app=leetcode id=1046 lang=python
#
# [1046] Last Stone Weight
#

# @lc code=start
import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        heapq.heapify(stones)
        # convert the minheap into maxheap
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            largest1 = heapq.heappop(max_heap)
            largest2 = heapq.heappop(max_heap)
            if largest1 == largest2:
                # when the max heap is empty, it should return 0 immediately
                if not max_heap:
                    return 0
                # if it is not empty, it can continue
                else:
                    continue
            # if the 2 largest numbers are not equal, it should add number into the max heap
            elif largest1 != largest2:
                newnumber = largest1 - largest2
                heapq.heappush(max_heap, newnumber)
        return -max_heap[0]
# @lc code=end

