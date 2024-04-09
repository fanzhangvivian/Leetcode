# 501 FindModein BinarySearchTree
## Intuition
- Based on the binary search tree, it is ordered as a list, so you can use the in-order traversal
- Compared with two related node, and update the count of the node
- Each step you should compare with the max count, and update the node of the max count

## Approach
- In-order traversal the binary tree and record each node count
- Use a current node to record previous node val and also compared with the val to record its count
- Compared with the max count in each step and update the max count 
- Use a list to record current max count node's value.Each time you find the greater count, you should remove the previous node in the list and just add new node 
- Return the final list


## Complexity
- Time complexity:
O(n)

- Space complexity:
O(1)