from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """
        We can create a deep copy with only the normal `.next` linkage
        by just doing one single forward pass. And while doing so, we
        should also create a hashmap where the key is the original node,
        and the value is the deep copy node.

        Then we can do another pass to create the random linkage. As we
        traverse forward in the original list, we will simultaneously know
        what the deep copy is for the parent node and the `.random` node.

        Now to link the random, we would have to be able to reference
        what links to what.

        Time Complexity: O(n)
            It's a two pass, so O(2n)

        Space Complexity: O(n)
            A hashmap of size n is needed to reference the copied nodes
        """
        if not head:
            return head


        hashmap = {}
        copy_head = Node(head.val)
        hashmap[head] = copy_head

        curr = head
        copy_curr = copy_head
        while curr:
            if curr.next:
                copy_next = Node(curr.next.val) if curr.next else None
            else:
                copy_next = None
            hashmap[curr.next] = copy_next
            copy_curr.next = copy_next
            curr = curr.next
            copy_curr = copy_curr.next

        # do random links
        curr = head
        copy_curr = copy_head
        while curr:
            if curr.random:
                copy_random = hashmap[curr.random]
            else:
                copy_random = None

            copy_curr.random = copy_random
            curr = curr.next
            copy_curr = copy_curr.next

        return copy_head
