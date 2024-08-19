#
# @lc app=leetcode id=860 lang=python
#
# [860] Lemonade Change
#

# @lc code=start
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        # 3situation: 
        # 1: bills = 5, no payback
        # 2. bills = 10, payback 5
        # 3. bills = 20, prior payback 5+10,then payback 5+5+5
        five = 0
        ten = 0
       

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                else:
                    five -= 1
                    ten += 1
            elif bill == 20:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif ten == 0 and five >= 3:
                    five -= 3
                else:
                    return False
        return True
                    
# @lc code=end

