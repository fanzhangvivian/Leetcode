#
# @lc app=leetcode id=998 lang=python
#
# [998] Maximum Binary Tree II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # Return a new TreeNode if tree is empty
        if not root:
            return TreeNode(val)
        # If val>root.val val 
        if val > root.val:
            # Create a new node with the value
            new_node = TreeNode(val)
            # Attach the current root as the left subtree of the new node
            new_node.left = root
            # Return the new node tree
            return new_node
        # If val < root.val
        # recursively call insertIntoMaxTree on the right subtree
        root.right = self.insertIntoMaxTree(root.right, val)

        return root
    
# @lc code=end

