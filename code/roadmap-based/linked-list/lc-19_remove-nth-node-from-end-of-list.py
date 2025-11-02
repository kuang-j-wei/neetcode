from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
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
