#
# @lc app=leetcode id=124 lang=python
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # Base case
        if not root:
            return 0
        
        # 以当前节点为起点的路径数量 + 递归左子树的路径数量 + 递归右子树的路径数量
        return max(self.traversal(root), self.pathSum(root.left), self.pathSum(root.right))
    
    def traversal(self, cur, path):
        # Base case
        if not cur:
            return 0
        # 记录路径
        path.append(cur.val)
        count = 0

        count = max(count, sum(path))
        if cur.left:
            # 向左递归，记录每一个向左递归路径的count，count是0或者1
            self.traversal(cur.left, path[:]) 
        if cur.right:
            # 向右递归，记录每一个向右递归路径的count，count是0或者1
            self.traversal(cur.right, path[:])
            
        return count 
# @lc code=end

