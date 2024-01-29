#
# @lc app=leetcode id=988 lang=python
#
# [988] Smallest String Starting From Leaf
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    # 1注意题干说的是字符串最小值，而不是数字之和最小值，所以要先将数字转返回字母，添加进列表里进行比较
    # 2 题干要求的是从叶子节点到根节点，所以添加进列表时 需要反转方向[::-1]
    # 3 字符串比较是从首位开始比较，即首位小则整体字符串小，即abc<bbc
    # 4将数字转换为字母 可以用chr函数和ord 
    # chr 是一个 Python 内置函数，用于将 Unicode 码点转换为对应的字符 
    # ord('a') 返回小写字母 'a' 的 Unicode 码点，将这两者相加后，chr 将结果转换为对应的字符。
    
    #递归法
    
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        path = []
        result = []
        return self.traversal(root, path, result)
        

    def traversal(self, cur, path, result):
        path.append(chr(cur.val + ord('a'))) #先将数字转返回字母，添加进列表里进行比较

        if not cur.left and not cur.right:
            result.append(''.join(path)[::-1]) #添加进列表时 需要反转方向[::-1]
            
        if cur.left:
            self.traversal(cur.left, path[:], result) #利用path[:] 新建一个list 从而进行回溯
        if cur.right:
            self.traversal(cur.right, path[:], result)
        
        smallespath = min(result)
        return smallespath
     
     #迭代法

    def smallestFromLeaf(self, root):
        stack, path_stack, result = [root], [[chr(root.val + ord('a'))]], []  #先将数字转返回字母添加进列表里

        while stack:
            cur = stack.pop()
            path = path_stack.pop()

            if not cur.right and not cur.left:
                result.append(''.join(path[::-1]))#添加进列表时 需要反转方向[::-1]
                smallestfromleaf = min(result)
            if cur.right:
                stack.append(cur.right)
                path_stack.append(path + [chr(cur.right.val + ord('a'))])
            if cur.left:
                stack.append(cur.left)
                path_stack.append(path + [chr(cur.left.val + ord('a'))])
        return smallestfromleaf



 
        
# @lc code=end

