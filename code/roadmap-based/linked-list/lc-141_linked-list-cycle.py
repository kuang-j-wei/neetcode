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