#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # create a default list of dictionary that if the key doesn't exsit, it could return empty list.
        anagram_map = defaultdict(list)

        for str in strs:
            sorted_str = "".join(sorted(str))
            anagram_map[sorted_str].append(str)
        
        return list(anagram_map.values())
        
# @lc code=end

