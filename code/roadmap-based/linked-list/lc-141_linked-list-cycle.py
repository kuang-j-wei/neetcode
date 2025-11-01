from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        We can continuously iterate through the linked list. Meanwhile
        we use a hashmap to keep track of nodes that we've visited
        before. Since this hashmap look up takes only O(1) time, we
        won't be adding additional time complexity as we are traversing
        through the linked list. When we've reached the end of the list
        where now the current pointer is pointer to Null, and we've not
        encountered a node that we've visited before, we can return
        False. Otherwise, if at any time a visited node is encountered
        we return True.

        Time Complexity: O(n)
            We iterate at worst over all nodes
        
        Space Complexity: O(n)
            At worst the visited hashmap can grow to the size of the
            input linked list
        """
        visited = set()
        
        curr = head
        while curr:
            if curr in visited:
                return True
            visited.add(curr)
            curr = curr.next
        return False


class SolutionFast:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        If there is a cycle, since this is a closed loop, the faster
        moving pointer is guaranteed to eventually catch up to the
        slower moving pointer. And if the speed of them differ by only
        one, then it would only take them the same number of iterations
        as the size of the cycle, because at each iteration the distance
        between the two pointers is being reduced by one. And the size
        of this cycle can be anywhere between 1 (self cycle) or the
        entire size of the linked list, if the cycle occurred from the
        end point to the start point.

        Time Complexity: O(n)
            We iterate at worst over all nodes
        
        Space Complexity: O(1)
            No additional space is needed
        """
        slow, fast = 0, 0
        
        # need current fast to exist, and fast.next to exist since we need fast.next.next in this current loop
        while fast and fast.next.next:  
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False
