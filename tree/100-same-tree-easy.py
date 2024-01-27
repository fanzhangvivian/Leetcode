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
    #递归法
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        elif p != None and q == None:
            return False
        elif p == None and q!= None:
            return False
        elif p.val != q.val:
            return False
        
        left_compare = self.isSameTree(p.left, q.left)
        right_compare = self.isSameTree(p.right, q.right)
        result = left_compare and right_compare

        return result

    #利用队列迭代法
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if p is None and q is None:
            return True
        queue = collections.deque([p, q])

        while queue:
            leftnode = queue.popleft()
            rightnode = queue.popleft()

            if leftnode is None and rightnode is None:
                continue
            elif leftnode is not None and rightnode is None:
                return False
            elif leftnode is None and rightnode is not None:
                return False
            elif leftnode.val != rightnode.val:
                return False
            
            queue.append(leftnode.left)
            queue.append(rightnode.left)
            queue.append(leftnode.right)
            queue.append(rightnode.right)

        return True
    

    #层序遍历法
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """    
        if p is None and q is None:
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

