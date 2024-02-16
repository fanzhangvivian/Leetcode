#
# @lc app=leetcode id=129 lang=python
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Iteration method by using Stack
        if not root:
            return 0
        stack = [root]
        path_stack = [[root.val]]
        result = []

        while stack:
            cur = stack.pop()
            path = path_stack.pop()
            if not cur.left and not cur.right:
                result.append(''.join(map(str, path))) # 添加的是string
            if cur.right:
                stack.append(cur.right)
                path_stack.append(path + [cur.right.val])
            if cur.left:
                stack.append(cur.left)
                path_stack.append(path + [cur.left.val])

        sumresult = sum(list(map(int, result))) # 要转为int的list

        return sumresult    

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Recursion
        # 建立收集路径和计算路径之和
        # 递归的要点：1.中左右递归
        # 往左右递归时，均需要回溯，利用path[:]新建列表，而不影响其他子树收集路径
        if not root:
            return 0
        path = []
        result = []
        return self.traversal(root, path, result)
    
    def traversal(self, node, path, result):
        path.append(node.val)
        if not node.right and not node.left:
            result.append(int(''.join(map(str, path))))
        if node.left:
            self.traversal(node.left, path[:], result)
        if node.right:
            self.traversal(node.right, path[:], result)

        return sum(result)

# @lc code=end

