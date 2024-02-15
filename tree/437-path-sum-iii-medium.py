#
# @lc app=leetcode id=437 lang=python
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        # Base case
        if not root:
            return 0
        
        # 以当前节点为起点的路径数量 + 递归左子树的路径数量 + 递归右子树的路径数量
        return self.traversal(root, [], targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
    
    def traversal(self, cur, path, targetSum):
        # Base case
        if not cur:
            return 0
        # 记录路径
        path.append(cur.val)
        count = 0

        if sum(path) == targetSum:
            count += 1   # 一旦路径之和=target count便+1
        if cur.left:
            # 向左递归，记录每一个向左递归路径的count，count是0或者1
            count += self.traversal(cur.left, path[:], targetSum) 
        if cur.right:
            # 向右递归，记录每一个向右递归路径的count，count是0或者1
            count += self.traversal(cur.right, path[:], targetSum)
            
        return count 


  
# @lc code=end

