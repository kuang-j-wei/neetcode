from typing import Optional


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
        and return the maximum path sum, which would take O(n^3) because
        the path can be any arbitrary two starting and end nodes, which
        already give us O(n^2) choices. Then the act of summing over
        these nodes would take another O(n), totaling O(n^3). To not get
        to this cubic time complexity, we have to reuse paths.

        As hinted by that [1, 2, 3] example, we will need to start from
        a leaf node when counting the sum, which inspires us to use a
        DFS algorithm. A node will either be a 'turning point', meaning
        it connects the left and right nodes paths, then add along its
        own node value to get the total path value. Note that for a case
        like this, this will be a complete
        path as it cannot then be combined with another other nodes (
        otherwise this "root" node will be connecting to three nodes,
        which isn't allowed in this path definition). Then another
        possibility is that this current node is just part of a path,
        so it could further contribute to a larger running sum as we
        account for nodes that are higher.

        So our approach would be, we would keep track of a global
        max_path variable, and every time we calculate the total path
        sum of a "root of subtree" path, we check whether this new sum
        surpasses the existing max_path. We then also consider another
        case where this node is just part of a larger path that will
        involve higher up nodes. In this case, we would need to check
        whether the left or right node offer a path that has a higher
        value. We then would add the current node value to the larger
        path and pass it upwards, which means we return this curr.val
        + max(left_path, right_path) in our depth first search function.

        Note that, because a node by itself is also considered a valid
        path, then if any of the left or child path ends up being
        negative, we could also just choose to not pursue these negative
        paths, and instead only return the current value. This can be
        handled by setting the left or right max to a floor number of 0.
        Then as we return `curr.val + max(left_path, right_path)`, we
        effectively would just be returning `curr.val`, in the case
        if both the left and right paths are negative, which effectively
        function as if we simply aren't traversing these left or right
        children paths.

        So in short, the "turning point" option, because of the 0 floor
        pruning implementation, we have effectively considered all four
        possibilities
            * The path only takes in the curr val itself
            * The path only takes in curr val and left child path
            * The path only takes in curr val and right child path
            * The path takes curr val and both left and right child
              paths
        And since we compare this turning point path to the global
        max_path, we have always been tracking the maximum path value
        possible through this entire DFS. And in the dfs function we
        only need to return "if we don't use this node as a turning
        point, what is the maximum possible path value this child node
        could pass up to its parent?", which would be the current node
        value, plus whichever is larger, left child or right child path.

        Then lastly, because the global max_path has been tracking the
        maximum path this entire time, we just need to call dfs(root)
        from the start, then at the end just return the max_path
        variable as the final answer.

        Time Complexity: O(n)
            Like a standard DFS, every node is visited once

        Space Complexity: O(h)
            The recursive stack for a DFS can at most grow to the height
            of the tree, which has a best case of O(log(n)) for a
            balanced tree, and O(n) for an extremely unbalanced tree.

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
            turning_point_path = left_path_sum + right_path_sum + curr.val
            # in this case, we've essentially terminated the path, so
            # compare it to the global path max to see if
            max_path = max(max_path, turning_point_path)


            # second is this is just a passing node, which takes the max
            # of either left path or right path, and this is what we
            # could offer up to the parent as the best option for the
            # parent to draw a path passing through this node
            passing_node_path = curr.val + max(left_path_sum, right_path_sum)


            return passing_node_path

        passing_path = dfs(root)
        return max(max_path, passing_path)

