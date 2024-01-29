#
# @lc app=leetcode id=101 lang=python
#
# [101] Symmetric Tree
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
    #层序遍历法 1.建立队列和用一个list接住每层的节点 2 如果每层节点数为奇数，直接返回false 3 如果节点为空，则添加到list的结果为None
    # 4 用list是否对称 判别每层是否是对称 5 若每层都对称，则返回True
    def isSymmetric(self, root):
        if root == None:
            return True
        
        queue = collections.deque([root.left, root.right])

        while queue:
            result = []
            queue_size = len(queue)
            if queue_size % 2 != 0:
                return False
            
            for i in range(queue_size):
                node = queue.popleft()
                if node:
                    result.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    result.append(None)
            
            if result != result[::-1]:
                return False
        
        return True
    


    #递归法
    # 1.确定递归函数的参数和返回值  2.递归终止条件，左右子节点为空或者其中一个为空或者不为空，但是不相等 
    # 3 进入递归的单层逻辑 左右节点不为空，且数值相等，进入下一层递归 比较外侧：左子树的左节点和右子树的右节点，内侧：左子树的右节点和右子树的左节点
    # 4 当外侧和内侧均为真时，则返回真，其中一个为假，则返回假
class Solution(object):
    def isSymmetric(self, root):
     """
     :type root: TreeNode
     :rtype: bool
     """
     if root == None:
          return True
     return self.compare(root.left, root.right) != -1
    
    def compare(self, right, left):
        if left is None and right != None:
            return -1
        elif left != None and right == None:
            return -1
        elif left == None and right == None:
            return 0
        elif left.val != right.val:
            return -1
        
        outside = self.compare(left.left, right.right)
        inside = self.compare(left.right, right.left)
        if outside == -1 or inside == -1 :
            return -1
        
        

        
    
    

# #迭代法 1.建立队列比较左右子树内外侧 2 左右子节点为空或者其中一个为空或者不为空，但是不相等 即为假； 若均为空节点，则继续
#     # 加入队列是 左子树的左节点，右子树的右节点，左子树的右节点，右子树的左节点 这样保证队列pop出来的俩节点是对称关系，并进行比较
# class Solution(object):
#     def isSymmetric(self, root):
        
#         if root == None:
#             return True
#         #建立一个空的队列 并把左右子树头节点添加进去
#         queue = collections.deque() #或者使用栈 st=[] 其实是一样的方法
#         queue.append(root.left)
#         queue.append(root.right)

#         while queue:
#             leftnode = queue.popleft()
#             rightnode = queue.popleft()
#             # 左节点，右节点都为空，说明对称 继续向下比较
#             if leftnode == None and rightnode == None:
#                 continue
#             #左右一个节点不为空，或者都不为空但数值不相同，返回false
#             elif leftnode != None and rightnode == None:
#                 return False
#             elif leftnode == None and rightnode != None:
#                 return False
#             elif leftnode.val != rightnode.val:
#                 return False
            
#             queue.append(leftnode.left) #加入左节点左孩子
#             queue.append(rightnode.right) #加入右节点右孩子
#             queue.append(leftnode.right) #加入左节点右孩子
#             queue.append(rightnode.left) #加入右节点左孩子
#         return True

        
# @lc code=end

