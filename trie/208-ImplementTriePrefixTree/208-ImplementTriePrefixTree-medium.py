#
# @lc app=leetcode id=208 lang=python
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
# class Trienode(object):
#     def __init__(self):
#         self.children = {}
#         self.isEnd = False
class Trie(object):
    # 1. use dict to restore each node and its children
    # 2. use a mark in the end of each string
    #insert car and cat like below
#     {
#     'c': {
#         'a': {
#             't': {
#                 '*': 1
#             },
#             'r': {
#                 '*': 1
#             }
#         }
#     }
# }

    def __init__(self):
        self.root = {}
       
    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
    
        cur = self.root

        for letter in word:
            if letter not in cur:
                cur[letter] = {}
            cur = cur[letter]
        cur["*"] = 1

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for letter in word:
            if letter not in cur:
                return False
            cur = cur[letter] 
        return "*" in cur

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for letter in prefix:
            if letter not in cur:
                return False
            cur = cur[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

