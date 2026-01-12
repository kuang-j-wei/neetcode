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
