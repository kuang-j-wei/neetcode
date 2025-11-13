from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        first check whichever head is the smaller value and assign it as
        the returning head. We then assign curr1 and curr2 (remember to
        move the smaller one forward). Then we can just continuously
        link nodes by checking which curr1 or curr2 have the smaller
        value

        Time Complexity: O(n)
            We only traverse through each node once

        Space Complexity: O(1)
            No additional memory was used
        """
        if not list1:
            return list2
        if not list2:
            return list1

        new_head = list1 if list1.val <= list2.val else list2
        curr = new_head
        curr1  = list1.next if list1.val <= list2.val else list1
        curr2  = list2.next if list2.val < list1.val else list2

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next

        if curr1:
            curr.next = curr1
        if curr2:
            curr.next = curr2

        return new_head