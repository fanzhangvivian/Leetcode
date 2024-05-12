#
# @lc app=leetcode id=77 lang=python
#
# [77] Combinations
#

# @lc code=start
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # Pruning method in backtacking!!
        # Example: n = 4, k = 2 output:[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
        # Pseudocode: 
        # 1. We need return a list which includs the right path that is a list
        # 2. we need a recursive function that generate all right combinations of k numbers
        # 3. The ending situation is that we find the k numbers of combination and add into the result
        # 4. The single-layer search logic is that for each number i ,we add it into the current combinations,
        # and the recursively generate all the combinations of next numbers
        # After that, we remove i from the current combination to backtracking and try the next number
        # 5. Pruning: When we found that the length of left numbers is less than the needed element's length
        # it means doesn't need any deeper search. we can stop the search so that we can save the time
       
        result = [] # 2d array
        self.backtracking(n, k, 1, [], result)
        return result
    
    def backtracking(self, n, k, startindex, path, result):
        if len(path) == k:
            result.append(path[:])
            return 
        for i in range(startindex, n-(k-len(path))+2): # Optimize the range
            # if the length of left element is less than the needed element's length
            # it means doesn't need any deeper search. 
            # This means pruning            
            path.append(i)
            self.backtracking(n, k, i+1, path, result)
            path.pop()


        
# @lc code=end

