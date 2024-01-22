#
# @lc app=leetcode id=110 lang=python
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #递归法
        # 第一 返回布尔值 第二步 Base case
        if root is None:
            return True

        if abs(self.getdepth(root.left) - self.getdepth(root.right)) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def getdepth(self, node):
        if node is None:
            return 0
        left_depth = self.getdepth(node.left) 
        right_depth = self.getdepth(node.right) 
        
        depth = 1 + max(left_depth, right_depth)
        return depth
        
        
            

# @lc code=end

