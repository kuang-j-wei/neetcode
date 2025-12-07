from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        We can traverse through the main tree from `root`, and as soon
        as the value match of the current node we are on in the main
        tree matches the root node value of the subRoot, we can then
        start a new sub-problem of checking whether two trees are
        identical. If they are, we can immediately return True. But if
        the two subtrees are not equal at this stage, we can also
        continue to check if any of the remaining subtree of the main
        root tree can match up to the subRoot. Otherwise, if we've
        exhausted all nodes in root, then we know that there is not
        a subtree that matches up.

        Time Complexity: O(n)
            We at most traverse through each node once

        Space Complexity: O(n)
            I use BFS which can at the widest point be O(n) for the
            queue length. The `isIdentiical` function uses DFS that has
            a recursive stack that will grow to the height of the two
            subtree problems, which would be O(1) for the last layer
            of the root tree, or could be at most O(h) as the main
            height of root, which again still could ve in worse case in
            O(n) space complexity and best case O(log(n)) for a balanced
            tree. In both cases though, we are bound by O(n) as the
            worst case as the space complexity.
        """
        queue = deque()
        if not root and subRoot:
            return False
        if not subRoot and root:
            return False

        queue.append(root)
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.val == subRoot.val:
                    if self.isIdentical(curr, subRoot):
                        return True

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return False

    def isIdentical(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2 or (root1.val != root2.val):
            return False

        return self.isIdentical(root1.left, root2.left) and self.isIdentical(root1.right, root2.right)

        # queue1 = queue()
        # queue2 = queue()

        # queue1.append(root1)
        # queue2.append(root2)

        # while queue1 and queue2:
        #     curr1 = queue1.popleft()
        #     curr2 = queue2.popleft()

        #     if curr1.val != curr2.val:
        #         return False


        # return True