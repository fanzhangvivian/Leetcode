#
# @lc app=leetcode id=100 lang=python
#
# [100] Same Tree
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
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
    
        if p == None and q == None:
            return True
        
        queue = collections.deque([p, q])
        

        while queue:
            queue_size = len(queue)

            if queue_size % 2 !=0:
                return False
            
            level_val = []
            for i in range(queue_size):
                node = queue.popleft()
                if node:
                    level_val.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    level_val.append(None)

            if level_val[:(queue_size)//2] != level_val[(queue_size)//2:]:
                return False
        
        return True

                


        
# @lc code=end

