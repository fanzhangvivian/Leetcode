#
# @lc app=leetcode id=394 lang=python
#
# [394] Decode String
#

# @lc code=start
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        cur_num = 0
        cur_string = ""

        for string in s:
            if string.isdigit():
                cur_num = cur_num * 10 + int(string)
            elif string == "[":
                stack.append(cur_string)
                stack.append(cur_num)
                cur_num = 0
                cur_string = ""
            elif string == "]":
                num = stack.pop()
                pre_string = stack.pop()
                cur_string = pre_string + num*cur_string
                
            else:
                cur_string += string
        return cur_string
# @lc code=end

