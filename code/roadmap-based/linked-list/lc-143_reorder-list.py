# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Because we are oscillating between using a node counted from the
        front, and a node counted from the back, we want to divide this
        linked list by two, then we can reverse the second half of the
        linked list, which would then allow us to iterate backwards.

        To split the linked list in half, we can use a slow and fast
        pointer approach, where the slow pointer advances one node at a
        time, and the fast pointer advances two nodes at a time. Because
        the fast pointer goes at twice the speed of the slow pointer, by
        the time it covers the full distance of the linked list, the
        slow pointer would only have the time to cover only half the
        distance, so it would be at the half point of the linked list.

        And because we start the reordering from the head, we want the
        first half (which includes the head) to be longer than the
        second half so that when we are relinking the nodes we don't run
        out of nodes in the first half first.

        As such, we will always call the node after the slow pointer the
        start of the second half of the linked list. So if the list is
        of even length, the two halves are of equal length, and if it's
        odd, then the second half is one node shorter.

        We can then reverse the second half by using a prev, curr, and
        tmp pointer solution. After the reversal, the last node of this
        reversed list will point to Null, which will let us properly
        terminate this linked list when traversing through the second
        half.

        Then we sever the link between the first half and the second
        half by assigning the `.next` of the end node of the first half
        to Null, which would then avoid a cycle forming between the
        first and second half of the node.

        Then we merge the two halves by alternating between the nodes
        from the head of the first half, and the new head of the
        reversed second half, which is the original tail of this linked
        list, doing so until the second half is fully traversed through.
        And because we already assigned the last node of the first half
        to connect to Null as its next node, this linked list will have
        a correct Null ending, as we always will end with the last node
        of the first half leftover, since we made the first half to be
        longer or equal length as the second half, so by the time we
        finish traversing the second half, we will also have traversed
        through the full first half.

        Time Complexity: O(n)
            We only do linear pass once in the slow and fast pointer
            split plus the reversing of the second half, then another
            forward pass for merging.

        Space Complexity: O(1)
            No additional space is used.
        """
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow.next is the start of the second half, so we need to
        # start reversing pointers. Create a dummy node so as we are
        # iterating through the reversed list we will hit a natural end
        prev = None
        curr = slow.next
        while curr:
            tmp = curr.next
            curr.next = prev
            # move curr to original curr.next
            # move prev to curr
            prev = curr
            curr = tmp

        # disconnect from second half from first
        slow.next = None

        # front and back one by one iteration until the back reversed
        # list reaches null
        tail = prev

        while tail:
            head_next_tmp = head.next
            head.next = tail
            tail_next_tmp = tail.next
            head = head_next_tmp
            tail.next = head
            tail = tail_next_tmp



class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        We want to alternate the linked list.

        In an ideal world, we would have two pointers one at the start
        and one at the end. Then at every increment, we would move the
        front pointer forward and the end pointer backward. But this
        would require us to memorize the "before" element for every
        singe node. We could use a hashmap to do this, where we key
        each element and its "before" as the value. This would require
        one forward pass of the linked list. And with this forward pass,
        we would have a pointer pointing at the last element. We will
        also keep two additional pointers that are the original "next"
        and the original "prior" element. We then can just link the
        front pointer to the end pointer, and the "prior end" to the
        "next front". Then we can move the front pointer to the current
        "next front" and the end pointer to the current "prior end".

        We repeat until the front_next and "prior_end" overlap, or
        that "prior_end" is on top of "current front". This means we've
        passed the middle point. Then if front_next and "prior end"
        overlap, we just assign `.next` as usual except point the next
        of front_next to Null. Otherwise, we point front.next to curr
        end, and point end.next to Null.


        Time Complexity: O(n)
            One forward pass, then each element is again visited at most
            once.

        Space Complexity: O(n)
            Hashmap is memorizing the prior element to every single
            element.
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

        # curr is now the null, and prior is the last element

        front = head
        end = prior

        # oscillate between front and back
        front_next = front.next
        end_next = priors[end]

        while front_next != end_next and front != end_next:
            front.next = end
            end.next = front_next

            front = front_next
            end = end_next

            front_next = front.next
            end_next = priors[end]

        if front_next == end_next:
            front.next = end
            end.next = front_next
            front_next.next = None
        if front == end_next:
            front.next = end
            end.next = None




