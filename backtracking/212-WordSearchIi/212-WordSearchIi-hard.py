#
# @lc app=leetcode id=212 lang=python
#
# [212] Word Search II
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:  # move the pointer until the last character in word
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.isWord = True  # find the leaf of the word

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # prefix tree
        # transfer the list of words into a prefix tree
        # and use DFS backtracking
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        ROWS, COLS = len(board), len(board[0])

        res, visit = set(), set() # mark the visited character, don't repeat in one word again

        def dfs(r, c, node, word): # the stored word:word, the current node
            if (r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visit or board[r][c] not in node.children):
                return
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            dfs(r-1, c, node, word)
            dfs(r+1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)

            visit.remove((r, c))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)

# @lc code=end

