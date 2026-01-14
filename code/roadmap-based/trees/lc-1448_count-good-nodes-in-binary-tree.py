# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        We can do a DFS traversal of the tree, and for every node, note
        the maximum value it has seen in its traversal path so far. Then
        at each node, we can compare to the max path value to see if
        we've seen a larger number in its path. If not, we can then add
        one to a number of valid path counter. The key idea here is that
        we don't necessarily have to keep a full record of the current
        chain that we are traversing on, just the maximum value of the
        chain. So the core idea is that, if we are appending the
        children of a node into the stack, then these children and the
        current node we are on, are on the same path. Therefore by
        comparing this "path max" value and the current node value, we
        are always correctly updating the path max value.

        Time Complexity: O(n)
            We visit every node in the tree once
        Space Complexity: O(h)
            The stack used to keep track of the DFS can at most grow to
            the height of the tree, so best case is O(log(n)) for a
            balanced tree, and O(n) for an extremely unbalanced tree
        """
        paths = 0
        stack = [(root, root.val)]

        while stack:
            curr, path_max = stack.pop()
            if curr.val >= path_max:
                paths += 1

            new_max = max(path_max, curr.val)

            if curr.right:
                stack.append((curr.right, new_max))
            if curr.left:
                stack.append((curr.left, new_max))
        return paths


class SolutionRecursive:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Base case is, if it's None, then return 0, because no valid
        path can be set on a Null node.

        Then we need to check if the current value is greater than or
        equal to the path_max. If it is, then the current node is
        considered a valid path. So we incur one additional path. Then
        we need to add this 1 with the sum of the left and right
        sub-problems by calling dfs on the two children, and at the same
        time pass on the current node value as the new path_max.
        Otherwise, we just need to return the left and right
        sub-problems, without needing to add 1 and we continue to pass
        on the existing path_max

        Time Complexity: O(n)
            Every node is visited once

        Space Complexity: O(h)
            The recursive stack can grow to the height of the tree. So
            O(log(n)) for a balanced tree and O(n) in the most extreme
            unbalanced tree case
        """
        def dfs(curr, path_max):
            if not curr:
                return 0

            if curr.val >= path_max:
                return 1 + dfs(curr.left, curr.val) + dfs(curr.right, curr.val)
            else:
                return dfs(curr.left, path_max) + dfs(curr.right, path_max)

        return dfs(root, root.val)

