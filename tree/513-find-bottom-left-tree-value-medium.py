#
# @lc app=leetcode id=513 lang=python
#
# [513] Find Bottom Left Tree Value
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
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #迭代法 找到每一行的第0位即为最左的节点
        if root is None:
            return 0
        queue = collections.deque([root])

        while queue:
            lenqueue = len(queue)
            for i in range(lenqueue):
                cur = queue.popleft()
                if i == 0:
                    result = cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        
        return result
        
        
# @lc code=end

