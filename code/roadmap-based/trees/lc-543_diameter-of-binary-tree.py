# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        The diameter of any single node is simply the height of the
        left subtree plus the height of the right subtree. Because the
        longest path from the deepest node as part of the left sub-tree
        to the current root node is simply the height of the left
        sub-tree, and the same logic follows for the right sub-tree as
        well. Then adding the two heights together results in the
        diameter, the longest combined path from one node connected
        through this node to another node. So if we can find the heights
        of every node's left and right subtrees, then we can know the
        diameter through every single node, thus returning the maximum
        diameter.

        We can recursively find the height of every subtree, where the
        base case is simply the Null node which has a height of 0. Then
        the height at every location is simply the maximum of its left
        and right subtrees, then plus one to account for the current
        node height.

        Once we have the left and right sub tree height, we can also
        calculate the diameter, and then we compare it to a global
        max_diameter to find out if the current diameter qualifies as
        the maximum diameter. Once all the subtree heights have been
        calculated and we've bubbled back up to the root node, we will
        have walked through the diameter of every single node and
        therefore we can return the max diameter encountered during our
        traversal.

        Time Complexity: O(n)
            Every single node is visited once in order to calculate the
            height at that point, thus time complexity is O(n)

        Space Complexity: O(h)
            The recursive stack can grow to the height of the binary
            tree.
            Best case is a balanced tree which is O(log(n)) worst case
            is a deep single sided tree which would be o(n)

        """
        self.max_diameter = 0

        def helper(curr):
            if not curr:
                return 0, 0
            left_diameter, left_height = helper(curr.left)
            right_diameter, right_height = helper(curr.right)
            curr_diameter = left_height + right_height
            curr_height = max(left_height, right_height) + 1
            self.max_diameter = max(self.max_diameter, curr_diameter)
            return curr_diameter, curr_height

        curr_diameter, curr_height = helper(root)

        return self.max_diameter


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        The diameter of any single node is simply the height of the
        left subtree plus the height of the right subtree. Because the
        longest path from the deepest node as part of the left sub-tree
        to the current root node is simply the height of the left
        sub-tree, and the same logic follows for the right sub-tree as
        well. Then adding the two heights together results in the
        diameter, the longest combined path from one node connected
        through this node to another node. So if we can find the heights
        of every node's left and right subtrees, then we can know the
        diameter through every single node, thus returning the maximum
        diameter.

        We can recursively find the height of every subtree, where the
        base case is simply the Null node which has a height of 0. Then
        the height at every location is simply the maximum of its left
        and right subtrees, then plus one to account for the current
        node height.

        Once we have the left and right sub tree height, we can also
        calculate the diameter, and then we compare it to a global
        max_diameter to find out if the current diameter qualifies as
        the maximum diameter. Once all the subtree heights have been
        calculated and we've bubbled back up to the root node, we will
        have walked through the diameter of every single node and
        therefore we can return the max diameter encountered during our
        traversal.

        Time Complexity: O(n)
            Every single node is visited once in order to calculate the
            height at that point, thus time complexity is O(n)

        Space Complexity: O(h)
            The recursive stack can grow to the height of the binary
            tree.
            Best case is a balanced tree which is O(log(n)) worst case
            is a deep single sided tree which would be o(n)

        """
        def helper(curr, max_diameter):
            if not curr:
                return 0, 0
            left_max_diameter, left_height = helper(curr.left, max_diameter)
            right_max_diameter, right_height = helper(curr.right, max_diameter)
            curr_diameter = left_height + right_height
            curr_height = max(left_height, right_height) + 1
            max_diameter = max(max_diameter, curr_diameter, left_max_diameter, right_max_diameter)
            return max_diameter, curr_height

        return helper(root, 0)[0]

