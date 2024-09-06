#
# @lc app=leetcode id=678 lang=python
#
# [678] Valid Parenthesis String
#

# @lc code=start
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 遍历两次，第一次顺序，第二次逆序。

        # 第一次遇到左括号加一，右括号减一，星号加一，最后保证cnt >= 0,也就是可以保证产生的左括号足够
        # 第二次遇到右括号加一，左括号减一，星号加一，最后保证cnt >= 0,也就是可以保证产生的右括号足够
        # 当两次遍历都是True，那么说明只有唯一解 那就是他们数量相等
        def help(a):
            count = 0
            for c in s if a == 1 else reversed(s):
                if c == "(": count += a
                if c == ")": count += -a
                if c == "*": count += 1
                if count < 0:
                    return False
            return True
        return help(1) and help(-1)

# @lc code=end

