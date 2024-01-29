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
        path.append(cur.val) #中
        if not cur.left and not cur.right:
            spath = '->'.join(map(str, path))
            result.append(spath) 
            return #停止条件
        if cur.left: #左
            self.traversal(cur.left, path, result)
            path.pop() # 当左子树递归完了之后，则回到根节点 path =最初的 path.append(cur.val)
        if cur.right: #右
            self.traversal(cur.right, path, result)
            path.pop() # 当右子树递归完了之后，则回到根节点 path =最初的 path.append(cur.val)

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
    
    # # 递归+隐形回溯 一
    def binaryTreePaths(self, root):
        result = []
        path = []
        if not root:
            return result
        self.traversal(root, path, result)
        return result
    def traversal(self, cur, path, result):
        path.append(cur.val)
        if not cur.left and not cur.right:
            spath = '->'.join(map(str, path))
            result.append(spath) #记住列表是append 添加， 字符串添加是 += str()
        if cur.left:
            self.traversal(cur.left, path[:], result)
            # 这里的path[:]意味着复制一个新的path路径出来，而不影响原来的path
            #通过产生不同的分支，所以也就起到了回溯的过程
        if cur.right:
            self.traversal(cur.right, path[:], result)
    

    #递归+隐形回溯二 利用字符串不可变，只能新建一个，进行回溯
    def binaryTreePaths(self, root):
        result = []
        path = '' #将路径定义为一个空的字符串
        if not root:
            return result
        self.traversal(root, path, result)
        return result
    def traversal(self, cur, path, result):
        path += str(cur.val)
        if not cur.left and not cur.right:
            result.append(path)
        if cur.left:
            self.traversal(cur.left, path + '->', result)
            # 因为path为''字符串，所以path+'->'就为一个新的字符串，就不会影响原来的path路径
        if cur.right:
            self.traversal(cur.right, path + '->', result)
     

    #迭代法： 利用一个stack遍历所有节点，一个stack存放对应的遍历路径，一个列表收集符合的路径
    def binaryTreePaths(self, root):
          stack, path_stack, result = [root], [str(root.val)], []

          while stack:
               cur = stack.pop()
               path = path_stack.pop()
               if not cur.left and not cur.right:
                    result.append(path)
               if cur.right:
                    stack.append(cur.right)
                    path_stack.append(path + '->' + str(cur.right.val))
               if cur.left:
                    stack.append(cur.left)
                    path_stack.append(path + '->' + str(cur.left.val))
            
          return result

    


           
# @lc code=end

