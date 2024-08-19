#
# @lc app=leetcode id=135 lang=python
#
# [135] Candy
#

# @lc code=start
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # 1.compare from left to right and update the counts when the 
        # right kids'rate>left kid's rate
        # 2.compare from right to left and update the counts when the 
        # left kid's rate>right kid's rate
        # the 2nd situation should gurantee kid's counts > left and right 
        # when the kid's rate is higher than them, so we should get the maximum value

        candy_vec = [1] * len(ratings)
        
        # 1st situation:from front to end, deal with the higher rate kid
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candy_vec[i] = candy_vec[i - 1] + 1
        
        # 2st situation:from end to front, deal with the higher rate kid
        for i in range(len(ratings)-2, -1, -1):  # begin with len(ratings)-2, cuz we can compare index[-1] and index[-2]
            if ratings[i] > ratings[i+1]:
                candy_vec[i] = max(candy_vec[i], candy_vec[i+1] + 1)
        
        result = sum(candy_vec)
        return result
# @lc code=end

