from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        We will do this in a two-pass way: we first check if we have k
        nodes in front for us to reverse. If there a k nodes available,
        we will reverse the linked list and return the reversed head
        and tail, so that they can be used for linkage with the previous
        and next sections. And because we need to link with the previous
        and next sections, before we do any reversing, we will also need
        to make sure we have the node right in front and right after the
        section that we are trying to reverse, so that we can complete
        the linkage. After properly linking with the before and after
        nodes of the k section that we just reversed, we move forward to
        the next node and continue checking whether we have enuogh nodes
        to reverse again. We do this until there are no nodes available
        to be reversed again.

        One tricky and critical implementation detail is that we have to
        switch the curr pointer that tracks the traversal in the linked
        list to the newly reversed tail in order for the positional
        tracking to be correct. Otherwise curr pointer will be pointing
        at a node that's already been reversed.

        Time Complexity: O(n)
            We traversed each node at most twice, once from checking if
            there are k remaining nodes in the list, and another from
            reversing
        
        Space Complexity: O(1)
            No additional space was used
        """
        if not head or not head.next or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head

        curr = dummy
        while curr:
            pre_node = curr
            for _ in range(k): 
                curr = curr.next
                if not curr:  # null check needs to be done after moving node, because we want to see if we went out of bound after moving
                    return dummy.next 
            post_node = curr.next
            reversed_head, reversed_tail = self.reverseKNodes(pre_node.next, k)
            pre_node.next = reversed_head
            reversed_tail.next = post_node
            curr = reversed_tail  # move the curr pointer to the right position, the new tail of the reversed linked list because curr was at the old tail which is now at the start after reversing

        return dummy.next


    def reverseKNodes(self, head, k):
        """
        k is inclusive, i.e. if k == 2 reverse head and its next node,
        which only involves one link
        """
        prev = None
        curr = head

        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev, head
