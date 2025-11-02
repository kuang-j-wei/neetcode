from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        We force left and right pointers to have a gap of n + 1, so that
        by the time r reaches past the end, l will be at the node right
        before the node that we are supposed to delete. We can think
        about if n = 1, then the distance between the Null at the end
        and the end of the node is exactly 1, and the end node is the
        node that we are supposed to be deleted, and the l pointer will
        be at the node in front of the end node. Then we just need to
        assign the left pointer node's next to itself's next next to
        remove the nth node counted from the back

        Time Complexity: O(n)
            We just need to traverse the entire linked list once

        Space Complexity: O(1)
            No additional space is used.
        """
        dummy = ListNode(None, next=head)

        l = dummy
        r = head

        for _ in range(n):
            r = r.next

        while r:
            l = l.next
            r = r.next

        l.next = l.next.next
        return dummy.next


class SolutionHash:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        This can be achieved if we know the "before" of a node.

        We can do one forward pass to store all the "before" of each
        node in a hashmap, the process of doing this will also allow us
        to reach the end of the linked list. Then we can count backwards
        n times, letting the current node be the node that we want to
        remove. Then we assign the "previous"'s next to the current
        node's next, effectively removing the current node. And if the
        curr node is pointing at the head of the array, we instead will
        just return the current node's next as the new head node.
        Otherwise, we return the original head node.

        Time Complexity: O(n)
            One forward pass to store all the "prior" nodes. Then at
            most another n of counting backwards.

        Space Complexity: O(n)
            Store all the prior node of each node in a hashmap takes up
            n space.
        """
        if not head.next:
            return None

        priors = {}
        prior = None
        curr = head

        while curr:
            priors[curr] = prior
            prior = curr
            curr = curr.next

        curr = prior
        prev = priors[curr]

        for _ in range(n - 1):
            curr = priors[curr]
            prev = priors[curr]


        if prev:
            prev.next = curr.next
        else:
            return curr.next

        return head
