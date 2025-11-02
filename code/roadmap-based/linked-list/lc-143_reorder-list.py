# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
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




