#
# @lc app=leetcode id=981 lang=python
#
# [981] Time Based Key-Value Store
#

# @lc code=start
import collections
class TimeMap(object):

    def __init__(self):
        self.time = collections.defaultdict(list)
        self.values = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.time[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        timestamps = self.time[key]
        if not timestamps:
            return ""
        if timestamp < timestamps[0]:
            return ""
        lo, high = 0, len(timestamps)
        while lo < high:
            mid = (lo + high) // 2
            if timestamps[mid] <= timestamp:
                lo = mid + 1
            else:
                high = mid
        return self.values[key][lo-1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

