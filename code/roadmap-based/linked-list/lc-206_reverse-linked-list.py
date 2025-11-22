# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        In the iterative version, we will save three pointers: prev,
        curr, and next. next is necessary because after we link
        curr.next to prev, we won't be able to directly access the next
        node. We will do this until curr is at a None, which means we
        have run out of all nodes, and we have reversed all links. We
        will also start with setting the first prev to be None, so when
        curr is on the original head, its next will correctly be set to
        None.

        Time Complextiy: O(n)
            We traverse every node exactly once only

        Space Complexity: O(1)
            No additional space was used
        """
        if not head or not head.next:
            return head

        curr = head
        prev = None
        while curr:
            nxt= curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        head.next = None
        return prev