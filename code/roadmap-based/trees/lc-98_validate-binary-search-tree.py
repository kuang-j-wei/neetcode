from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        We can just recursively traverse through the entire tree, and
        at every node, check whether its left and right nodes satisfy
        the BST condition. We can do this traversal with BFS, since
        """
        queue = deque()
        queue.append(
            (
                root,
                (float(-inf), float(inf))
            )
        )

        while queue:
            for _ in range(len(queue)):
                curr, min_max_range = queue.popleft()
                min_range, max_range = min_max_range
                if curr.val < min_range or curr.val > max_range:
                    return False

                if curr.left:
                    if curr.val <= curr.left.val or (curr.left.val < min_range or curr.left.val > max_range):
                        return False
                    queue.append(
                        (
                            curr.left,
                            (
                                (min_range, min(curr.left.val, max_range))
                            )
                        )
                    )
                if curr.right:
                    if curr.val >= curr.right.val or (curr.right.val < min_range or curr.right.val > max_range):
                        return False
                    queue.append(
                        (
                            curr.right,
                            (
                                (max(curr.right.val, min_range), max_range)
                            )
                        )
                    )
        return True