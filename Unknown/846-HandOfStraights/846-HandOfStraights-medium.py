#
# @lc app=leetcode id=846 lang=python
#
# [846] Hand of Straights
#

# @lc code=start
from collections import Counter


class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0:
            return False
        handcount = Counter(hand)

        for hand_start in sorted(handcount.keys()):  # 从每一个顺子里最小的手牌开始遍历
            while handcount[hand_start]:  # 只要还有最小手牌，就继续寻找是否存在顺子
                for hand_end in range(hand_start, hand_start + groupSize):
                    if not handcount[hand_end]:
                        return False  # 说明要找的那张牌没了
                    handcount[hand_end] -= 1  # 减少一张手牌
        return True
# @lc code=end

