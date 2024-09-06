#
# @lc app=leetcode id=227 lang=python
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stringstack = []
        pre_op = "+"
        cur_num = 0
        s += "+"

        for string in s:
            if string.isdigit():
                cur_num = cur_num * 10 + int(string)
            elif string == " ":
                pass
            else:
                if pre_op == "+":
                    stringstack.append(cur_num)
                elif pre_op == "-":
                    stringstack.append(-cur_num)
                elif pre_op == "*":
                    prenum = stringstack.pop()
                    stringstack.append(prenum * cur_num)
                elif pre_op == "/":
                    # prenum = stringstack.pop()
                    stringstack.append(int(stringstack.pop() / cur_num))
                cur_num = 0
                pre_op = string
        return sum(stringstack)
                
# @lc code=end

