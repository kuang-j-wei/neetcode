# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        We can just search through the entire tree to find all paths
        and return the maximum path sum. To not get to the O(2^n)
        exponential time complexity, we have to reuse paths. As we
        accumulate along the path, we can always store the current path
        sum, then when we are taking on a new node, we don't have to
        calculate the path sum from the very first node.

        We most likely will need to start from a leaf node when counting
        the sum based off of that [1, 2, 3] example. Same with that
        root = [-10,9,20,null,null,15,7] example. We can start from node
        7, then to 20, then it traces up to 20, then to 15. But if a
        leaf node is negative, then we wouldn't want to include to
        include it, unless it's the smallest negative in this entire
        tree, which is possible too. If the addition of a node decreases
        the current sum,
        """
        return None

