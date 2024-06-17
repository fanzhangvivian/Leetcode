#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 1. use hash map to record used element in each column searching, 
        # each element in deep searching can be used once
        # 2. ending case: when the path length = nums list length
        # 3. each leave searching still start from 0 not startIndex
        path = []
        result = []
        self.backtracking(nums, path, [False]* len(nums), result)
        return result

    def backtracking(self, nums, path, used, result):
        if len(path) == len(nums):
            result.append(path[:])
            return 
        for i in range(len(nums)):
            if used[i]:
                continue

            used[i] = True
            path.append(nums[i])
            self.backtracking(nums, path, used, result)
            path.pop()
            used[i] = False

# @lc code=end

