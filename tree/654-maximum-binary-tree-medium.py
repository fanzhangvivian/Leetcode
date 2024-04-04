#
# @lc app=leetcode id=654 lang=python
#
# [654] Maximum Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # 确定递归函数的参数和返回值
        #参数传入的是存放元素的数组，返回该数组构造的二叉树的头结点，返回类型是指向节点的指针
        # 01 Base case：Define the Termination Condition
        if not nums:
            return None
        # 02 Define the max value of nums ,and divide left and right array 
        root_val = max(nums)
        root_index = nums.index(root_val)
        root = TreeNode(root_val)
        # 02 recursion
        root.left = self.constructMaximumBinaryTree(nums[:root_index])
        root.right = self.constructMaximumBinaryTree(nums[root_index + 1:])
        # 03 Return root point
        return root
# @lc code=end

