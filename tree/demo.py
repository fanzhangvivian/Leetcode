# Iteration method by using Stack
        # Base case
        if not root:
            return False
        # stack contain pair of <node pointer, path value>
        stack = [(root, root.val)]
        while stack:
            node, path = stack.pop()
            # If find the leaf point and the sum = targetsum, return True
            if not node.left and not node.right and path == targetSum:
                return True
            # Pushing the node right point into stack, and also record the path value of the code
            if node.right:
                stack.append((node.right, path + node.right.val))
            # Pushing the node left point into stack, and also record the path value of the code
            if node.left:
                stack.append((node.left, path + node.left.val))
        return False