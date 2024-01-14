#
# @lc app=leetcode id=145 lang=python
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #递归法
        if not root:
            return []
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)

        return left + right + [root.val]
    
        #迭代法 利用中左右入栈，中右左出栈，再将result反转倒序
        if not root:
            return []
        stack = [root]
        res =[]
        while stack:
            #中节点先处理
            node = stack.pop()
            res.append(node.val)
            #处理左节点
            if node.left:
                stack.append(node.left)
            #处理右节点
            if node.right:
                stack.append(node.right)
        return res[::-1]
# @lc code=end

