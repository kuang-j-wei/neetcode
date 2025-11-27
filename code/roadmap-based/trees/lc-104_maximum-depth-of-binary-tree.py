from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        We can do a breath first search to go layer by layer to traverse
        the tree, and add 1 to the depth whenever we are at a new layer.

        Time Complexity: O(n)
            Every node is still visited once, so time complexity is O(n)
        Space Complexity: O(n) at the worst case, O(1) at the best case
            The queue would grow to the largest at the last layer which
            is of size O((n+1)/2) because of the geometric sum
            derivation where n = 2^(h + 1) - 1. But if the tree is very
            imbalanced with one single long deep chain, then the queue
            would only be constrained to the size of about 1 or 2
        """
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        queue = deque()
        queue.append(root)
        depth = 0

        while queue:
            depth += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return depth


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Max depth can be think of as a recursive sub-problem. The root's
        left and right sub-tree will each have their own max depth too.
        And we can take the max between the two, and add one to the
        depth to account for the current root node, to get the full
        tree's max depth. We can break down the problem recursively
        into sub-trees until we've hit the leaf nodes where their
        children nodes are None. When the node entered is a Null, we
        return 0 as the depth, and that's the base case.


        Time Complexity: O(n)
            Every node is still visited once, so time complexity is O(n)
        Space Complexity: O(h) for the recursive stack
            Height of tree is O(log(n)) for the best case of a balanced
            binary tree O(n) at worst case

        """
        if not root:
            return 0

        left_max_depth = self.maxDepth(root.left)
        right_max_depth = self.maxDepth(root.right)
        return 1 + max(left_max_depth, right_max_depth)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        We do a pre-order depth first traversal and keep track of the
        current depth at every node. And we also separately track a
        max_depth variable so at every node we check whether max_depth
        or the current depth is larger. Once we've visited all nodes,
        we will have also found the maximum depth

        Time Complexity: O(n)
            Every node is still visited once, so time complexity is O(n)
        Space Complexity: O(n) at the worst case, O(1) at the best case
            The queue would grow to the largest at the last layer which
            is of size O((n+1)/2) because of the geometric sum
            derivation where n = 2^(h + 1) - 1
        """
        if not root:
            return 0

        stack = [(root, 1)]
        max_depth = 1

        while stack:
            curr, curr_depth = stack.pop()
            max_depth = max(curr_depth, max_depth)
            if curr.right:
                stack.append((curr.right, curr_depth + 1))
            if curr.left:
                stack.append((curr.left, curr_depth + 1))

        return max_depth
