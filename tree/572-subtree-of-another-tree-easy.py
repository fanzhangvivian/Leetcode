#
# @lc app=leetcode id=572 lang=python
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        #如果root为空，则subRoot不在里面
        if root == None:
            return False
        # 直接从根节点开始比较
        if self.comparetree(root, subRoot):
            return True
        #从根节点的左子树或者右子树比较
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def comparetree(self, r, s):
        if r == None and s == None:
            return True
        elif r == None or s == None:
            return False
        # 当根节点值相等且左右子树一样，才返回True
        elif r and s:        
            return r.val == s.val and self.comparetree(r.left, s.left) and self.comparetree(r.right, s.right)

        
# @lc code=end

