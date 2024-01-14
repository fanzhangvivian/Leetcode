#
# @lc app=leetcode id=94 lang=python
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #递归法
        if not root:
            return [] #注意要返回一个空的list
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        return left + [root.val] + right
    
        #迭代法 利用指针迭代访问到最左子树节点 再入栈
        if not root:
            return []
        stack = []
        res = []
        cur = root
        while stack or cur:
            if cur:
                stack.append(cur) #用指针迭代访问最左子树节点
                cur = cur.left #Left node
            #到达栈顶处理栈顶节点
            else:
                cur = stack.pop()
                res.append(cur.val) 
                # 取栈顶元素的右节点
                cur = cur.right
        return result
    


        
# @lc code=end

