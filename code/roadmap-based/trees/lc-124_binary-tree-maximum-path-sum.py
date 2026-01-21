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
        7, then to 20, then it traces up to 20, then to 15. A node will
        either be a middle node in a path, meaning it connects the left
        and right nodes' paths. Or it would be a middle node of a path.
        """
        max_path = float("-inf")

        def dfs(curr):
            nonlocal max_path
            if not curr:
                return 0

            # if not curr.left and not curr.right:
            #     return curr.val

            left_path_sum = max(0, dfs(curr.left))
            right_path_sum = max(0, dfs(curr.right))
            # two cases, one is this is a middle node, so summing left
            # and right and itself
            middle_node_path = left_path_sum + right_path_sum + curr.val
            # in this case, we've essentially terminated the path, so
            # compare it to the global path max to see if
            max_path = max(max_path, middle_node_path)


            # second is this is just a passing node, which takes the max
            # of either left path or right path
            passing_node_path = curr.val + max(left_path_sum, right_path_sum)


            return passing_node_path

        passing_path = dfs(root)
        return max(max_path, passing_path)

