from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Sorting would take O(n log(n))

        But nums1 and nums2 are already sorted

        We know the median will be at mid = (m + n) / 2

        If int, it's mid - 1 plus m + 1. If float, then its (m + n) // 2
        and there is only one number that we need to find
        """
        return None
