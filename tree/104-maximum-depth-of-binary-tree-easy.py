#
# @lc app=leetcode id=104 lang=python
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #递归法
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        max_depth = 1 + max(left, right)

        return max_depth

        #迭代法
        if not root:
            return 0
        queue = collections.deque([root])
        depth = 0

        while queue:
            len_queue = len(queue)
            depth += 1

            for i in range(len_queue):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return depth
        
# @lc code=end

