## Approach ##
- Slide the valid replace window
- Bullet point: how to find the valid window
    - 1. Find the most frequency in the window
    - 2. Use the current window length subscribe the most frequency number;
    - 3. If it is smaller and equal to k, it indicates that it is a valid window; since the replacement number is smaller and equal to k. right pointer continue slide for longer window. Also update the current max length of the window
    - 4. If it is bigger than k, it indicates that it is a unvalid window since the replacement number is bigger.Then slide the left pointer to ensure the window is valid. In the meanwhile,the frequency of the left pointer should reduce 1