#
# @lc app=leetcode id=669 lang=python
#
# [669] Trim a Binary Search Tree

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        #递归法
        if root == None:
            return None
        if root.val < low:
            # 寻找符合区间[low, high]的节点
            return self.trimBST(root.right,low,high)
        if root.val > high:
            # 寻找符合区间[low, high]的节点
            return self.trimBST(root.left, low, high)
        #用root.left & root.right 接住符合条件的左右孩子
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
        
        #迭代法
        if root == None:
            return root
        #将root放进[low, high]左闭右闭区间里
        while root and (root.val < low or root.val > high):
            if root.val < low:
                root = root.right
            else:
                root = root.left
        # 修减root的左子树
        cur = root
        #如果左子树比low小，就将cur的左子树的右子树接到cur上
        while cur:
            while cur.left and cur.left.val < low: 
                cur.left = cur.left.right
            cur = cur.left
        # 修减root的左子树
        cur = root
        #如果右子树比high大，就将cur的右子树的左子树接到cur上
        while cur:
            while cur.right and cur.right.val > high:
                cur.right = cur.right.left
            cur = cur.right

        return root
        
        
# @lc code=end

