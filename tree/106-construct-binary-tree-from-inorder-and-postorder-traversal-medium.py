#
# @lc app=leetcode id=106 lang=python
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # Base case 
        if not postorder:
            return None 
        # Find the root value from postorder
        root_val = postorder[-1]
        # Create the root 
        root = TreeNode(root_val)
        # Find the seperate index by inorder
        seperate_index = inorder.index(root_val)
        # Find the left and right by seperate index in inorderlist
        inorder_left = inorder[:seperate_index]
        inorder_right = inorder[seperate_index + 1:]
        # Find the left and right by using the length of inoderleft and inorderright
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left): len(postorder) - 1]
        # Recursion root left and right
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        return root

        
# @lc code=end

