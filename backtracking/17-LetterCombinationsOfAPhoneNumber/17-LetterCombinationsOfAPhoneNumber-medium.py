#
# @lc app=leetcode id=17 lang=python
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = [] 
        # Handle the empty string case
        if digits == "": 
            return result
        self.backtracking(digits, 0, "", result)
        return result
    
    def backtracking(self, digits, index, string, result):
        # A map to store the letters corresponding to each digit
        lettermap = {0: "", 1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno",
                     7: "pqrs", 8: "tuv", 9: "wxyz"}
        # when index is greater than the biggest index, it means the right number combiantion, so it should return
        # The digits's length represent the depth of the search
        if index == len(digits): # !!!It should be stoped until out of the digits range
            result.append(string)
            return 
        # Get the letters from each digit
        digit = digits[index]
        letters = lettermap[int(digit)]
        # The letters length represent the breadth of the search
        for i in range(len(letters)):
            string += letters[i]
            # Recursively generate combination for the next digit
            self.backtracking(digits, index+1, string, result)
            string = string[:-1]
# @lc code=end

