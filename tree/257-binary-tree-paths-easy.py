#
# @lc app=leetcode id=257 lang=python
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def traversal(self, cur, path, result):
        path.append(cur.val)
        if not cur.left and not cur.right:
            spath = '->'.join(map(str, path))
            result.append(spath)
        if cur.left:
            self.traversal(cur.left, path, result)
            path.pop()
        if cur.right:
            self.traversal(cur.right, path, result)
            path.pop()

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        path = []
        if not root:
            return result
        self.traversal(root, path, result)
        return result


        
# @lc code=end

