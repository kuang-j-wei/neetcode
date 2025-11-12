from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Since each is linked list is already sorted, we can start from
        each head, order them into an ascending order, then traverse one
        node forward, and then compare them all again.

        But the problem here is that in some linked list, their first
        layer may already be larger than the second layer of some other
        list, so this would cause a problem as well

        Brute force would just traverse through every single node and
        put them all into a long list, sort them, which would take
        O(k * n * log(k * n)) where n is the average length of each
        linked list.

        But each linked list is already sorted, so we should need to do
        this repeated sorting work and we should try to take advantage
        of this sorted fact.
        """
        return None
