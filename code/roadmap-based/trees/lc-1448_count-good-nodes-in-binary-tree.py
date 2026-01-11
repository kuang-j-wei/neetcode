# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Maybe we can do a DFS traversal of the tree, keep the current
        running chain, and check if this current chain contains a max
        value that's greater than the current node we are on

        The difficult part is to keeping the entire chain. For example
        in the example case they gave, when we are on chain [3, 4, 1],
        we know that we've reached a leaf node, therefore we need to pop
        1, but we should only pop one time to keep the [3, 4], and then
        add 5 into the chain
        """
        paths = 1
        return paths
