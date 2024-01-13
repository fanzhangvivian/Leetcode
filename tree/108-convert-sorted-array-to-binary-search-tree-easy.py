#
# @lc app=leetcode id=108 lang=python
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def traversal(self, nums, left, right):
        #递归法
        # 定义为左闭右闭区间
        #当左节点大于右节点 就终止，说明没有节点在数组里
        if left > right:
            return None
        #找到数组的中间节点，如果数组是偶数，调用的是左边的节点，但佐还是右都是一样的
        mid = (left + right) // 2
        #将中间节点定为root节点
        root = TreeNode(nums[mid])
         #注意区间是左闭右闭
        root.left = self.traversal(nums, left, mid - 1)
        root.right = self.traversal(nums, mid + 1, right)
        #返回root
        return root
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # 再调用traversal函数，并注意同样是左闭右闭区间
        root = self.traversal(nums, 0 , len(nums) - 1)
        return root

# @lc code=end

