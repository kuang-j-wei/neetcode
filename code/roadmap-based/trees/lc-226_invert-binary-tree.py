# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        We can just recursively keep calling the invertTree function
        on the left and right sub nodes until we are left with no more
        leaf node, in which case we can return itself.

        And as the inverted sub-trees are returned, we then swap the
        left and right node assignment

        Lastly, we return the original root, as all the subtrees are
        inverted. This would cause the inversion to "bubble up" and at
        last the top root will be returned, with all its subtrees
        inverted.

        Time Complexity: O(n)
            Since every node is traversed once
        
        Space Complexity: O(log(n)) for best case, O(n) worst case
            The recursive stack would reach the size of the depth of the
            tree, which is log(n), assuming a balanced binary tree. But
            it can reach O(n) for the worst case of a skewed tree
        """
        if not root:
            return root

        inverted_left = self.invertTree(root.left)
        inverted_right = self.invertTree(root.right)
        root.right = inverted_left
        root.left = inverted_right
        return root