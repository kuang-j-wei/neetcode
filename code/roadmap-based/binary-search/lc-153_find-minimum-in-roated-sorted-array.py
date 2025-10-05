from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        If it was already sorted, then the element
        before it will always be smaller, until
        you hit a number where the element before
        it is not smaller, then you know that you've
        identified the minimum

        We could divide an conquer, and find the mid
        inflection point, then the problem is solved.

        The key is to know which half to eliminate
        in order to find the right half.
        """
        n = len(nums)

        mid = n // 2
        return None