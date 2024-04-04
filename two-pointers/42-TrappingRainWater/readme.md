# Intuition
Two Pointer Technique: To begin with the two-pointer technique, which utilizes two pointers left and right to represent the left and right boundaries of the array. 
# Approach
- **Maintaining Maximum Heights**: Additionally, you need to maintain two variables left_max and right_max to keep track of the maximum height encountered at the current positions of the left and right pointers, respectively. Initially, both these variables are set to 0.
- **Iterative Pointer Movement:** 
  Within a loop, you iteratively move these pointers, comparing the heights at the current positions. If height[left] < height[right], it indicates that the left boundary's height is lower, allowing us to determine the amount of water that can be stored at the current left position. We update left_max, accumulate the water that can be stored at the current position into water, and move the left pointer to the right. 
- Conversely, if height[left] >= height[right], it signifies that the right boundary's height is lower. We update right_max, accumulate the water that can be stored at the current position into water, and move the right pointer to the left.
- **Returning the Result**: Finally, when the left and right pointers meet, it indicates the completion of one full traversal. At this point, water contains the total amount of trapped water, which is returned as the result.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(1)

# Code
```python
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_max = 0
        right_max = 0
        left, right = 0, len(height) - 1
        water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water
```