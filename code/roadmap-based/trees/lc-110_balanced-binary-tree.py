# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        We need to recursively find the height at every node, which
        would also mean finding the height of its two sub trees, and
        the current height is simply the maximum of the two subtrees'
        heights plus 1.

        And during this calculation process, we can also check the
        difference between the left and right sub=trees. And if the
        height difference is more than 1, we send a signal up the
        recursive stack to alert that we've already found two left and
        right sub-trees that differ for more than 1 in height so once we
        pop back up to the root node we can return False. Otherwise, we
        are safe to return True

        Time Complexity: O(n)
            Every node is still visited once because we calculate the
            height at every single node

        Space Complexity: O(h)
            The recursive stack can grow to the maximum height of the
            tree, which in best case is O(log(n)) for a balanced tree,
            and O(n) for a highly unbalanced linear chain

        """

        def helper(curr):
            if not curr:
                return 0

            left_height = helper(curr.left)
            right_height = helper(curr.right)
            if left_height == -1 or right_height == -1:
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1

        return False if helper(root) == -1 else True
