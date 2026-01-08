# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        (Note that we are already guaranteed that p and q will both be in
        the tree. And note that this is a BST not just a randomly
        ordered binary tree. And all values in this BST are unique.)

        To be an ancestor of two nodes, the two nodes have to both be
        descendants of a this ancestor node. And note that a node can be
        a descendant of itself, so a node can be its own ancestor.

        From these properties, we know that a root node will always be
        a common ancestor of any two nodes in this tree, because all
        nodes will trace back to it at the root, so it's an ancestor to
        any nodes in this tree, including the root node itself. It's
        just not guaranteed to be the lowest ancestor.

        So we can always start at the root, and then traverse down to
        see if we can find any lower common ancestor node.

        Now because this is a BST, we can know which direction we need
        to head down to in order to find p and q based on how large they
        are compared to the current common ancestor node (which again,
        will be the root node to start). If both p and q are smaller
        than the current ancestor node, we know that we can head down to
        the left subtree since both nodes will be in the left subtree,
        and we can now move the common ancestor to this left child node
        of the current ancestor node. With the same logic, we can move
        to the right subtree if both p and q are of greater value. Then

        Now if the current ancestor node is in between the values of p
        and q, then we know that we can't possibly head down to either
        left or right subtree and still find a common ancestor, because
        we will fail to find one of the two nodes in any of the left or
        right subtrees, since they belong in two separate branches.
        Therefore we know we've found the lowest common ancestor and we
        can return this current common ancestor node.

        Finally, for the edge case that if one of p or q nodes is of the
        same value of the current common ancestor, we also know that we
        can't further descend down to either direction, since then we
        would be missing one of the p or q nodes. 

        Time Complexity: O(h)
            We would only need to traverse the height of the tree since
            we only search for either left or right subtrees. So the
            best case would be O(log(n)) for a balanced BST, but can at
            worst be O(n) for an unbalanced subtree that's just a linked
            list.
            
        Space Complexity: O(1)
            No additional memory is used

        """
        lowest = root
        small_child = p if p.val < q.val else q
        big_child = p if p.val > q.val else q


        while lowest:
            if lowest.val<= big_child.val and lowest.val >= small_child.val:
                return lowest
            
            if small_child.val < lowest.val and big_child.val < lowest.val:
                lowest = lowest.left
            else:
                lowest = lowest.right
        return None
