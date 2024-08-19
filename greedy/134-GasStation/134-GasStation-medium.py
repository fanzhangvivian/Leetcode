#
# @lc app=leetcode id=134 lang=python
#
# [134] Gas Station
#

# @lc code=start
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # 当前累加rest[i]的和curSum一旦小于0，起始位置至少要是i+1，因为从i之前开始一定不行。
        # 全局最优：找到可以跑一圈的起始位置。
        # The current accumulated sum, curSum, from rest[i] should be reset 
        # if it becomes less than 0, because starting from any index before i+1 would definitely not work."
        # current difference obtained by subtraction: gas[i]-cost[i]
        # record the curdifferent, once it becomes negative, we should start from next one

        cur_sum = 0  # current accumulated sum of remaining gas
        total_sum = 0  # total remaining gas
        start = 0

        for i in range(len(gas)):
            cur_sum += gas[i] - cost[i]
            total_sum += gas[i] - cost[i]

            if cur_sum < 0:  # current accumulated sum <0
                start = i + 1 # update the start index
                cur_sum = 0

        if total_sum < 0:  # total accumulated sum<0, it means we can't run a circle
            return -1
            
        return start
# @lc code=end

