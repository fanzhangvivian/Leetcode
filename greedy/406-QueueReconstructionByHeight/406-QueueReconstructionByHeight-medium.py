#
# @lc app=leetcode id=406 lang=python
#
# [406] Queue Reconstruction by Height
#

# @lc code=start
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # 按身高高度排序
        # 局部最优：优先按身高高的people的k来插入。这样顺序操作后，其他的后面的一定能满足，因为都比前面的小
        # 全局最优：最后都做完插入操作，整个队列满足题目队列属性

        people.sort(key=lambda x:(-x[0], x[1])) # 先按高度排序，同样的就按k个数从小到大排序
        que = [] # creat a new queue to return the result

        # insert by the second element k of people
        # the same height is front when he with smaller k
        for p in people:
            que.insert(p[1], p)
        return que

# @lc code=end

