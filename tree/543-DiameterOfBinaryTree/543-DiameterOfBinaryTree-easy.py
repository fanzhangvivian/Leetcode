#
# @lc app=leetcode id=543 lang=python
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxdepth(root)
        return self.diameter
    
    def maxdepth(self, root):
        if not root:
            return 0
        if root.left:
            left = self.maxdepth(root.left)
        else:
            left = 0
        if root.right:
            right = self.maxdepth(root.right)
        else:
            right = 0
        self.diameter = max(self.diameter, right + left)

        return 1 + max(left, right)

     
# @lc code=end

