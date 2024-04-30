#
# @lc app=leetcode id=1448 lang=python
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.maxcount(root, root.val, 0)

    def maxcount(self, node, pre, count):
        if node is None:
            return count
        if node.val >= pre:
            count += 1
            pre = node.val
        count = self.maxcount(node.left, pre, count)
        count = self.maxcount(node.right, pre, count)
        return count

# @lc code=end

