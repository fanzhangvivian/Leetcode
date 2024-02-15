#
# @lc app=leetcode id=112 lang=python
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        # Recursion 
        # Base case
        if not root:
            return False
        # create a path to collect the root point to leaf point
        path = []
        return self.traversal(root, path, targetSum)
    
    def traversal(self, node, path, targetSum):
        # Record the node value to the path
        path.append(node.val)
        # If find the leaf point and the sum of path equal target ,return True
        if not node.left and not node.right and sum(path) == targetSum:
            return True

        if node.left: # Left Recurison 
            # return the left recursion result !!!Remember to return the result of Left Recurison
            if self.traversal(node.left, path[:], targetSum): 
                return True
        if node.right:
            # return the right recursion result !!!Remember to return the result of Left Recurison
            if self.traversal(node.right, path[:], targetSum):
                return True
        return False



class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        # Iteration method by using Stack
        # Base case
        if not root:
            return False
        # stack contain pair of <node pointer, path value>
        stack = [(root, root.val)]
        while stack:
            node, path = stack.pop()
            # If find the leaf point and the sum = targetsum, return True
            if not node.left and not node.right and path == targetSum:
                return True
            # Pushing the node right point into stack, and also record the path value of the code
            if node.right:
                stack.append((node.right, path + node.right.val))
            # Pushing the node left point into stack, and also record the path value of the code
            if node.left:
                stack.append((node.left, path + node.left.val))
        return False

# @lc code=end

