#
# @lc app=leetcode id=111 lang=python
#
# [111] Minimum Depth of Binary Tree
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
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #迭代法————层序遍历法
        if not root:
            return 0
        queue = collections.deque([root])
        depth = 0
        while queue:
            depth += 1
            
            len_queue = len(queue)

            for i in range(len_queue):
                node = queue.popleft()
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                if node.right is None and node.left is None:
                    return depth
        return depth
    
        #递归法
        if root is None:
            return 0
        
        if root.right is None and root.left is not None:
            return 1 + self.minDepth(root.left)
            
        if root.right is not None and root.left is None:
            return 1 + self.minDepth(root.right)
        
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
             
        
# @lc code=end

