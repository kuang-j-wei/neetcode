# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        So we would have to traverse to the the left starting node, then
        reverse the linked list until we reach right.

        The tricky part here is that we need to link the node before the
        left node to the newly reversed head, and the tail of the newly
        reversed linked list, to the original node after the right.

        To efficiently do this, I will traverse to right before the left
        node, and set a pointer to this node. And continue to travel to
        right after the right node, and also create a pointer to this
        node. Then I will start reversing linked list from
        left_prev.next. And after the reversal I will also set the
        tail.next to the after_right node. And return the original head

        And to handle the edge case of where left = 1, I will create a
        dummy node to point to the original head. This way even if
        left = 1, left_prev will still be set to dummy, therefore after
        the reversal, this dummy will then be linked to the new reversed
        head.

        Lastly, we will just return dummy.next since that's the true
        head.

        Time Complexity: O(n)
            For the right - left reversed section the nodes are traveled
            twice. So at most we would traversed every node twice, which
            is still O(n) time complexity
        
        Space Complexity: O(1)
            No additional memory used other than the two left_prev and
            right_next pointers, so it doesn't scale with the input
        """
        if not head or not head.next:
            return head

        dummy = ListNode(None)
        dummy.next = head
        curr = dummy
        for _ in range(left - 1):  # advance left - 1 times would get you to left node, and we want the previous to left, so left - 2, but add 1 for dummy
            curr = curr.next
        left_prev = curr
        
        for _ in range(right - left + 2):  # advance 1 time to get to left node, then advance right - left more times to get to the tail, then move one more to the next
            curr = curr.next
        right_next = curr

        new_head, tail = self.reverse_linked_list(left_prev.next, right - left + 1)
        left_prev.next = new_head
        tail.next = right_next
     
        return dummy.next

    def reverse_linked_list(self, head, k):
        prev = None
        curr = head
        tail = head

        for _ in range(k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # remember in a normal reverse linked list curr would already be
        # at a Null, so it's prev that's the old tail, which is the new
        # head
        new_head = prev 
        return new_head, tail