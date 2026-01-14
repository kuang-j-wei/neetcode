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
        the BST condition. Note though, that we not only need to check
        the immediate nodes' conditions, but we also need to make sure
        that every node in the left and right subtree of a node is below
        or greater than this node, respectively. So we have to memorize
        a minimum and maximum range that a node is allowed to take on,
        given its parent history. 

        We will use a queue to perform BFS, and instead of only pushing
        nodes themselves into the queue, we will also pass on the min
        max range, and the min max range will get updated as we push
        new nodes into the queue. For a left child, we know that the max
        range is now limited by the current node's value. Conversely for
        a right child, the min range is also limited by the current
        node's value as well.
        
        
        Time Complexity: O(n)
            Every node is traversed once
        
        Space Complexity: O(w)
            The queue can at most grow to the widest layer of the tree,
            which could be best case O(1) in an extremely unbalanced
            tree, or worst case O(n/2) for a balanced tree
        """
        queue = deque()
        queue.append(
            (
                root,
                (float(-inf), float(inf))  # first node, don't need to have any limit to the range
            )
        )

        while queue:
            for _ in range(len(queue)):
                curr, min_max_range = queue.popleft()
                min_range, max_range = min_max_range
                if curr.val <= min_range or curr.val >= max_range:
                    return False

                if curr.left:
                    queue.append(
                        (
                            curr.left,
                            (
                                (min_range, min(curr.val, max_range))
                            )
                        )
                    )
                if curr.right:
                    queue.append(
                        (
                            curr.right,
                            (
                                (max(curr.val, min_range), max_range)
                            )
                        )
                    )
        return True