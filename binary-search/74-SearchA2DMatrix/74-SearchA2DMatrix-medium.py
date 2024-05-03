#
# @lc app=leetcode id=74 lang=python
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Convert the matrix into a array 
        # 
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m*n-1
        while left <= right:
            # Get the index of the middle number in the array
            mid = (left + right) // 2
            # Return the middle row and col by divmod funciton
            # divmod() function in Python returns the quotient 
            # and remainder when the first number is divided by the second.
            mid_row, mid_col = divmod(mid, n)
            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
# @lc code=end

