from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        The key here is to consider the "merge two sorted lists" problem,
        then we will merge two lists together at a time. This will
        effectively reduce the number of times we do merge down to
        log(k). Thus if on average there are n elements in a linked
        list, the total operations will be O(n log(k)).

        Time Complexity: O(n log(k))
            Each merging two sorted linked lists will take O(n) time,
            and we only need to do it log(k) times since we are dividing
            by half of k each time we merge all lists
        
        Space Complexity: O(k)
            The temporary storage of next_lists can at most take k / 2
            pointers of the linked lists
        """
        if not lists:
            return None
        if len(lists) < 2:
            return lists[0]

        while len(lists) >= 2:
            next_lists = []
            for i in range(0, len(lists) - 1, 2): # at most reaching len(lists) - 2, which makes i and i + 1 valid because it gets to len(lists) - 1
                new_head = self.mergeTwoLists(lists[i], lists[i + 1])
                next_lists.append(new_head)
            if len(lists) % 2 != 0:
                next_lists.append(lists[-1])
            lists = next_lists

        return lists[0]


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

