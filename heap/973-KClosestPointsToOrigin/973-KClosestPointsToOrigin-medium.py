#
# @lc app=leetcode id=973 lang=python
#
# [973] K Closest Points to Origin
#

# @lc code=start
import math
import heapq

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # creat a function return the distance of x,y
        def custom_compare(x, y):
            return (x**2 + y**2)
        
        heap = []
        if k == len(points):
            return points
        else:
            # create a max heap
            # add the number of k item into heap compared with the negative number
            for i in range(k):
                heapq.heappush(heap, (-custom_compare(points[i][0], points[i][1]), points[i]))
            # compared with the remaining tuple and update the heap
            for j in range(k, len(points)):
                if -custom_compare(points[j][0], points[j][1]) > heap[0][0]:
                    heapq.heappushpop(heap, (-custom_compare(points[j][0], points[j][1]), points[j]))
            # use a list to return all the heap[1] elements
            result = []
            for m in range(len(heap)):
                result.append(heap[m][1])
            return result


        
        
# @lc code=end

