#
# @lc app=leetcode id=222 lang=python
#
# [222] Count Complete Tree Nodes
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
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #递归法
        #利用的是普通二叉树递归
        if not root:
            return 0
        left_count = self.countNodes(root.left)
        right_count = self.countNodes(root.right)
        return 1 +left_count + right_count

        #层序遍历————迭代法
        #利用的是普通二叉树层序遍历
        if not root:
            return 0
        
        queue = collections.deque([root])
        count = 0
        while queue:
            len_queue = len(queue)
            count += len_queue

            for i in range(len_queue):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return count


        #利用完全二叉树属性进行递归
        #如果是满二叉树，节点数则为2**深度 - 1，要先判断深度是否一致，如果一致则直接返回
        if not root:
            return 0
        left_depth = 1
        right_depth = 1
        left = root.left
        right = root.right
        while left:
            left = left.left
            left_depth += 1
        while right:
            right = right.right
            right_depth += 1

        if left_depth == right_depth :
            return 2**left_depth - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
     
               
# @lc code=end

