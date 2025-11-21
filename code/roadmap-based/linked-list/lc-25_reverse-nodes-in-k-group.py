from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        As we are iterating forward, we can reverse the link as we go.
        while keeping a pointer to the "current head", which will be the
        first node in these k nodes. And if the current node we are on
        is going to be the tail of the newly reversed sub-list, then we
        will save its next before reversing. After reversing, we will
        point the original k head to the tail.next that we saved. In
        addition, if this is the first sublist that we reversed, then
        we will also make this current tail node as the new head. And we
        move onto the previously saved tail.next as the current node as
        we iterate. And if in this reversing link process, we see that
        we've reached the end of the list, then we would need to go
        back to reversing the links again. This also means that we will
        always have to keep a pointer on the previous reversed k list's
        new tail so we could complete this final reversal if we've run
        out of space.

        Time Complexity: O(n)
            We only traverse through the list once
        
        Space Complexity: O(1)
            No additional space was used
        """
        if k == 1:
            return head
    
        if not head:
            return head

        curr = head
        first_reversed = False
        pre_pre_reverse_head = None 
        while curr:
            pre_pre_reverse_head = pre_reverse_head if pre_pre_reverse_head else None
            pre_reverse_head = curr
            
            for _ in range(k - 1):
                prev = curr
                if curr.next.next:
                    next = curr.next.next
                else:
                    break
                    # and enter the reversal phase
                curr = curr.next
                curr.next = prev
            
            
            pre_reverse_head.next = next
            pre_pre_reverse_head.next.next = curr
            previous_tail = curr
            curr = next

            if not first_reversed:
                head = previous_tail
                first_reversed = True
            
        return head            

