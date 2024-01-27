#
# @lc app=leetcode id=559 lang=python
#
# [559] Maximum Depth of N-ary Tree
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
import collections
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        #递归法
        if not root:
            return 0
        max_depth = 1
        for child in root.children:
            max_depth = max(max_depth, self.maxDepth(child) + 1)

        return max_depth
    
        #迭代法
        if not root:
            return 0
        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            for i in range(len(queue)):
                node = queue.popleft
                for child in node.children:
                    queue.append(child)
        return depth
    
        #栈 stack
        if not root:
            return 0
        max_depth = 0
        stack = [(root, 1)]

        while stack:
            node, depth = stack.popleft
            max_depth = (max_depth, depth)
            for child in node.children:
                stack.append((child, depth + 1))
        
        return max_depthdepth

# @lc code=end

