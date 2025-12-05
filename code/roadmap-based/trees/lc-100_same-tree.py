from typing import Optional
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        We need to check if the two trees are exactly the same. We can
        simply traverse the both trees, for example using breadth first
        search. Then as long as the two values don't match, only one
        value is None, or we run out of nodes in one of the trees first,
        it means the two are not the exact same trees. Otherwise, we
        will successfully traverse the two trees fully, and we can then
        return True

        Time Complexity: O(n)
            We traverse the trees each exactly once
        
        Space Complexity: O(n)
            The queue will be the widest in the last layer, which is
            roughly the size of O(n/2)
        """
        # if p is None and q is None:
        #     return True
        # if ((p is None) ^ (q is None)) or p.val != q.val:
        #     return False

        queue_1 = deque()
        queue_2 = deque()

        queue_1.append(p)
        queue_2.append(q)

        while queue_1 and queue_2:
            n1 = len(queue_1)
            n2 = len(queue_2)
            for _ in range(n1):
                try:
                    curr_1 = queue_1.popleft()
                except:
                    return False
                try:
                    curr_2 = queue_2.popleft()
                except:
                    return False
                
                if (curr_1 is None) ^ (curr_2 is None):
                    return False
                elif curr_1 is None and curr_2 is None:
                    continue
                elif curr_1.val != curr_2.val:
                    return False
                
                
                queue_1.append(curr_1.left)
                queue_1.append(curr_1.right)
                queue_2.append(curr_2.left)
                queue_2.append(curr_2.right)
        return True


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        We need to check if the two trees are exactly the same. We can
        simply traverse the both trees, for example using depth first
        search. Then as long as the two values don't match, only one
        value is None, or we run out of nodes in one of the trees first,
        it means the two are not the exact same trees. Otherwise, we
        will successfully traverse the two trees fully, and we can then
        return True

        Time Complexity: O(n)
            We traverse the trees each exactly once
        
        Space Complexity: O(h)
            The DFS stack size will grow to the depth of the tree, which
            in best case would be O(log(n)) for a balanced tree, and
            worse case is O(n) for an extremely skewed tree
        """
        # if p is None and q is None:
        #     return True
        # if ((p is None) ^ (q is None)) or p.val != q.val:
        #     return False

        stack_1 = []
        stack_2 = []

        stack_1.append(p)
        stack_2.append(q)

        while stack_1 and stack_2:
            curr_1 = stack_1.pop()
            curr_2 = stack_2.pop()

            if (curr_1 is None) ^ (curr_2 is None):
                return False
            elif curr_1 is None and curr_2 is None:
                continue
            elif curr_1.val != curr_2.val:
                return False
                
                
            stack_1.append(curr_1.left)
            stack_1.append(curr_1.right)
            stack_2.append(curr_2.left)
            stack_2.append(curr_2.right)
        return True
