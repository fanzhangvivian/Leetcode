#
# @lc app=leetcode id=491 lang=python
#
# [491] Non-decreasing Subsequences
#

# @lc code=start
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        path = []
        self.backtracking(nums, 0, path, result)
        return result
    
    def backtracking(self, nums, startIndex, path, result):
        if len(path) > 1:
            result.append(path[:]) # put the current path into result
            # dont return, because we have to interate all the leaf node
        
        # use hash map to check whether the element is used or not
        used = [0] * 201
        for i in range(startIndex, len(nums)):
            # if next element is smaller or the element is used before
            if (path and nums[i] < path[-1]) or used[nums[i] + 100] == 1:
                continue
            # Mark the used element 
            used[nums[i] + 100] = 1
            
            path.append(nums[i])
            self.backtracking(nums, i+1, path, result)
            path.pop()
# @lc code=end

