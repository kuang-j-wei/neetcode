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
            curr = nxt 
        return prev


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        The base case will just be a singular node (or None), because
        there is nothing to be reversed, so we can just return the input
        head node itself.

        So we can recursively call reverse on a smaller and smaller
        sublist, until we are returned with just the last node itself.

        But now we need to link this last node to its previous node.

        The key spirit in the recursive solution is that when a "later"
        node is returned, the previous node is still linked to this next
        node. So we can just call curr.next.next to set the nex tlink
        of this later node to this previous node itself, and then we
        severe the existing next link from the head.next link.

        Time Complexity: O(n)
            We traverse through all nodes once
        
        Space Complexity: O(n)
            The recursive call stack has to grow to the same size as the
            linked list itself
        """
        if head is None or head.next is None:
            return head
        
        new_head = self.reverseList(head.next)
        # need to reverse the pointer from the newly reversed list's tail to the original head caller
        head.next.next = head # head.next is the new tail of the reversed linked list; so we need to set its next back to current head
        head.next = None
        
        return new_head
