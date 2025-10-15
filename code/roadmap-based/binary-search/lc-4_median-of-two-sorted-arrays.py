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
        m = len(nums1)
        n = len(nums2)

        if (m + n) / 2 is int:
            # need two elements
            mid_m = m // 2
            mid_n = n // 2

            left_1 = nums1[:mid_m]
            right_1 = nums1[mid_m:]

            left_2 = nums2[:mid_n]
            right_2 = nums2[mid_n:]

            left_elements = (m + n) / 2 if (m + n) / 2 is int else (m + n + 1) / 2

            if len(left_1) + len(left_2) == left_elements:
                if max(left_1) <= min(right_2) and max(right_1) <= min(left_1):
                    return (nums1[mid_m] + nums2[mid_n]) / 2

            # if at the border move to only one array

            
        else:
            # only need one element
            return None
