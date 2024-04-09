#
# @lc app=leetcode id=501 lang=python
#
# [501] Find Mode in Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # creat current count and current node to record each iteration
        self.count = 0
        self.current = None
        # record the max_count in each step
        self.max_count = 0
        # creat a list to record max_count node value
        self.result = []

        self.traversal(root)
        return self.result

    def traversal(self, root):
        # since the binary tree is ordered, we can use in-order traversal
        if root is None:
            return [0]
        self.traversal(root.left)
        # record the current node's count
        if root.val == self.current:
            self.count += 1
        else:
            self.count = 1
        # update the current node
        self.current = root.val
        # comparied with the current max_count 
        if self.count > self.max_count:
            # remember to update the max_count's node 
            # by remove the previous node in the list
            self.max_count = self.count
            self.result = [root.val]
        elif self.count == self.max_count:
            self.result.append(root.val)
        self.traversal(root.right)
        return

# @lc code=end

