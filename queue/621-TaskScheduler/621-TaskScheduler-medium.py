#
# @lc app=leetcode id=621 lang=python
#
# [621] Task Scheduler
#

# @lc code=start
import collections

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # 1.if it should be seperated by at least n, it should have a n+1 slot size to put each number
        # 2.find the maximum frequency element, and there should be at least (maximum frequency-1) numbers of slot
        # 3. the last slot's elements depend on the maximum frequency number
        #     Ex: {A:6,B:4,C:2} n = 2
        #     [A, B,      C],
        #     [A, B,      C],
        #     [A, B,      idle],
        #     [A, B,      idle],
        #     [A, idle,   idle],
        #     [A   -        - ],
        # slot size = 3, last slot's elements just has 1 element(A) inside
        # 4.but If ans (calculated minimum time intervals) is less than the number of tasks, then it means tasks
        #  can be scheduled back-to-back without needing idle time. 
        freq = collections.Counter(tasks)
        max_freq = max(freq.values())
        freq = list(freq.values())
        max_freq_count = 0
        i = 0
        while i < len(freq):
            if freq[i] == max_freq:
                max_freq_count += 1
            i += 1
        ans = (max_freq - 1) * (n+1) + max_freq_count
        return max(ans, len(tasks))
# @lc code=end

