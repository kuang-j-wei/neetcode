from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Since the array is constrained to value [1 to n] and the array
        itself is of length n + 1, we can consider each value as a
        pointer pointing to another value in the array. In other words,
        we think of each value as an "index". So if a value is a
        duplicate, it means that multiple nodes will point to this same
        index, thus this is the start of the cycle, because a cycle in
        this linked list will always have two nodes pointing at it, as
        if no node has at least two incoming edges, then it means this
        entire array is one cycle, which is impossible because we would
        need a node to point to "0" but no value in this array will ever
        be 0.

        So we can think of the linked list as two portions, one is
        "before the cycle" and another is "the cycle".

        If we use a slow and fast pointer approach, the two pointers are
        guaranteed to meet somewhere in the cycle, as the fast pointer
        will enter it first but then continue to run in a loop. And once
        the slow pointer enters the loop, we can call the distance
        between the slow and fast pointer to be k; then it would only
        take k more iterations for the fast pointer to catch up to the
        slow pointer.

        Once we have this meeting point, by Floyd's algorithm we know
        that the start of the cycle, which is defined as having multiple
        nodes pointing to it can be found when we start a pointer from
        this meeting point, and another pointer from the head of the
        linked list, advancing them one step at a time until them meet,
        the new meeting point is the start of the cycle, in which we
        return this value.

        Floyd's algorithm can be proven to be true - let the distance
        from head to start of cycle be F, and let the length of the
        cycle to be C, and the distance from the meeting point to the
        start of the cycle be x. Slow pointer will take F + (C - x) to
        get to the meeting point. Fast pointer will take F + nC + (C-x)
        steps to the meeting point, where it loops though the cycle n
        times. Since fast pointer is twice the speed of the slow
        pointer, t_s = d_s / s, and t_f = d_f / 2s, and t_f == t_s, so
        2 * d_s = d_f; so 2 * (F + c - x) = F + nC + (C - x); then
        F + (1 - n)C - x = 0; F = x + (n - 1) * C

        So the pointer starting form the head will take F steps forward,
        meanwhile the pointer starting from the meeting point will do
        the same, which is F steps. Then it will reach x, and do (n-1)
        loops of the cycle, which will land itself back at the starting
        point, thus the two pointers will meet at exactly the starting
        node of the cycle.

        Time Complexity: O(n)
            We only traverse through the entire linked list once, so
            O(n).

        Space Complexity: O(1)
            No additional space is used.
        """
        # first use slow and fast pointer to get to the cycle meeting
        # point
        slow = 0
        fast = 0

        # then take one step further, so the start of the while loop
        # then are not already overlapping
        slow = nums[slow]
        fast = nums[nums[fast]]  # index once to move forward, then use the value to index/moves forward again

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # now they overlap, we start from the head and another from the
        # meeting point until the two pointers meet

        curr = 0
        while curr != slow:
            slow = nums[slow]
            curr = nums[curr]

        return curr