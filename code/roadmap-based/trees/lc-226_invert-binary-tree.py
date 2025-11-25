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


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        To invert the binary tree iteratively, we can do a breadth first
        search approach. At every layer, we add its leaf nodes to the
        queue so we can traverse through them in the next layer. We then
        swap these two leaf nodes' positions, and we move onto the next
        layer

        Time Complexity: O(n)
            Every node is visited once
        
        Space Complexity: O(n)
            We store pointers to the nodes in a queue, so the additional
            space needed would only depend on the size of the queue. If
            the tree is highly unbalanced, then at each layer there
            would only be two nodes. But for a balanced tree, the
            deepest layer would have the most number of nodes at roughly
            n/2 nodes. This is because at each layer we have 2^0, 2^1,
            ..., 2^h nodes. Since the total number of nodes is 1 + 2 + 4
            + ... + 2^h, n = 2^(h + 1) - 1

            n = 2^(h + 1) - 1
            n + 1 = 2^(h + 1)
            log(n + 1) = h + 1
            h = log(n+1) - 1

            So the last layer is
            2 ^ h = 2^(log(n+1) - 1) = 2^log(n+1) / 2 = (n + 1) / 2

            Which simplifies to O(n / 2) = O(n)
        """
        from collections import deque
        
        queue = deque()
        if root:
            queue.append(root)

        while queue: 
            for _ in range(len(queue)):
                curr = queue.popleft()
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
                curr.left, curr.right = curr.right, curr.left

        return root