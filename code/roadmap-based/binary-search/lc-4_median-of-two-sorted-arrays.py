from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        For both arrays, we want to divide each into left and right
        partitions. We need the maximum element of the left partition
        of one array to be smaller than the minimum element of the right
        partition of the other array. This will ensure that all elements
        in the left partitions are smaller than the all elements in the
        right partition.

        To do this, we will take the smaller array and do a middle
        partition. Then in the other array, we just take the first x
        elements, where x equals to the number of elements we need in
        the left partition in order to divide the combined array into
        half proportions.

        And when we find that the ordering condition is not met, we move
        move the half partition point higher or lower, depending on the
        breakage condition. If we know that the left partition numbers
        are too big, we move to the left. Otherwise we move to the
        right. We can even do this until we've covered the entire
        smaller array, and we will then move to the next.
        """
        m = len(nums1)
        n = len(nums2)

        total_amount = m + n
        half_amount = total_amount // 2

        A, B = nums1, nums2

        if m > n:  # make sure A is always the smaller array
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            # binary search the smaller array
            mid = (l + r) // 2   # len(3), mid point index 1; 2 elements; len(5), len(5); need 4; 2 on small array, need 2 more; 4 - 1 = 3
            left1 = A[:mid]
            right1 = A[mid:]

            left2 = B[:half_amount - mid + 1]
            right2 = B[half_amount - mid + 1:]

            # check if left portion of small array's max value is smaller
            # than the min value of the right portion of the big array
            if left1[-1] <= right2[0] and left2[-1] <= right1[0]:
                if total_amount % 2 == 0:  # even
                    return (max(left1[-1], left2[-1]) + min(right1[0], right2[0])) / 2
                else:
                    return min(right1[0], right2[0])

            if left1[-1] > right2[0]:
                r = mid - 1
            if left2[-1] > right1[0]:  # need to reduce B array, so take more in array 1
                l = mid + 1


        # if (m + n) / 2 is int:
        #     # need two elements
        #     mid_m = m // 2
        #     mid_n = n // 2

        #     left_1 = nums1[:mid_m]
        #     right_1 = nums1[mid_m:]

        #     left_2 = nums2[:mid_n]
        #     right_2 = nums2[mid_n:]

        #     left_elements = (m + n) / 2 if (m + n) / 2 is int else (m + n + 1) / 2

        #     if len(left_1) + len(left_2) == left_elements:
        #         if max(left_1) <= min(right_2) and max(right_1) <= min(left_1):
        #             return (nums1[mid_m] + nums2[mid_n]) / 2

        #     # if at the border move to only one array


        # else:
        #     # only need one element
        #     return None

if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 3]
    nums2 = [2]

    print(s.findMedianSortedArrays(nums1, nums2))
