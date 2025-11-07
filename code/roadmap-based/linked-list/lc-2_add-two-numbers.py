from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        The first digit would be 1st * 10**0, then plus 2nd * 10**1,
        then plus 3rd * 10**2

        We repeat the same procedure for the second linked list. Then we
        add up the two numbers.

        Now we need to construct the linked list, which we can achieve
        by converting the added sum into a string, and iterate from its
        back, and link with the digit in its front, and continue until
        we've traversed all digits from the back.

        Time Complexity: O(n)
            We traverse l1 and l2 each in one pass. Then traversing the
            digits of their sum would also take another O(n + 1)
        
        Space Complexity: O(1)
            No additional space was used
        """
        l1_num = 0
        curr = l1
        power = 0
        while curr:
            l1_num += curr.val * (10 ** power)
            curr = curr.next
            power += 1
        
        l2_num = 0
        curr = l2
        power = 0
        while curr:
            l2_num += curr.val * (10 ** power)
            curr = curr.next
            power += 1
        
        new_sum = l1_num + l2_num
        sum_str = str(new_sum)

        head = ListNode(int(sum_str[-1]))
        curr = head
        for val in sum_str[-2::-1]:
            curr.next = ListNode(int(val))
            curr = curr.next
            
        return head
