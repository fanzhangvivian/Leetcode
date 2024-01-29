#
# @lc app=leetcode id=113 lang=python
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        #递归法：参考257题 建立收集路径和满足targetsum的路径列表
        # 递归的要点：1.中左右递归 2 往左右递归时， 均需要回溯，利用path[:]新建列表，而不影响其他子树收集路径

        if not root:
            return []
        path = []
        result = []
        self.traversal(root, path, targetSum, result)
        return result
    
    def traversal(self, cur, path, targetSum, result):
        path.append(cur.val)
        if not cur.left and not cur.right:
            if sum(path) == targetSum:
                result.append(path)
        if cur.left:
            self.traversal(cur.left, path[:], targetSum, result)
        if cur.right:
            self.traversal(cur.right, path[:], targetSum, result)
     
     #迭代法
     #要注意path_stack记录路径的是各个路径List，而不是值，所以path_stack = [[root.val]]
     # 列表中数字相合并，则是list.append(list  + list) 
    def pathSum(self, root, targetSum): 
          if not root:
               return []
          stack, path_stack, result = [root], [[root.val]], [] #注意path_stack = [[root.val]] 是建立多个列表

          while stack:
               cur = stack.pop()
               path = path_stack.pop()

               if not (cur.left or cur.right):
                    if sum(path) == targetSum:
                         result.append(path)
               if cur.right:
                    stack.append(cur.right)
                    path_stack.append(path + [cur.right.val]) #注意此处写法 是列表相合并
                    
               if cur.left:
                    stack.append(cur.left)
                    path_stack.append(path + [cur.left.val])
                    
          return result
        
# @lc code=end

