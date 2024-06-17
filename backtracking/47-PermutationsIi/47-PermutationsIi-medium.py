#
# @lc app=leetcode id=47 lang=python
#
# [47] Permutations II
#

# @lc code=start
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # bulletpoint: if the element is used in same level and 
        # the current element == current-1 element, it should pass
        # 1. use hash map to record used element in each column searching, 
        # each element in same level searching can be used once 
        # and same element in same level can't be used even it doesn't be used before
        # 2. ending case: when the path length = nums list length
        # 3. each leave searching still start from 0 not startIndex

        nums.sort()
        result = []
        path = []
        self.backtracking(nums, path, [False]*len(nums), result)
        return result

    def backtracking(self, nums, path, used, result):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if (i>0 and nums[i] == nums[i-1] and not used[i-1]) or used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            self.backtracking(nums, path, used, result)
            path.pop()
            used[i] = False
# @lc code=end

