#
# @lc app=leetcode id=538 lang=python
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    #迭代法
    def __init__(self):
        self.pre = 0
    def travserl(self,root):
        stack = []
        cur = root

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.right #右
            else:
                cur = stack.pop() #中
                cur.val += self.pre #将pre节点的值更新到cur的值上
                self.pre = cur.val #移动pre节点 记录cur的值
                cur = cur.left  #左
        
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.pre = 0
        self.travserl(root)
        return root
        
    
    #递归法
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.pre = 0 #pre指针赋值为0
        self.traversal(root)
        return root
    def traversal(self, cur):
        if cur == None:
            return None
        self.traversal(cur.right) #右
        cur.val += self.pre #中 把pre的值相加到cur上
        self.pre = cur.val #更新pre的值为cur的值
        self.traversal(cur.left) #左

# @lc code=end

