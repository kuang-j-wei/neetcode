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

            Amax = A[mid] if mid >= 0 else float("-inf")
            Amin = A[mid + 1] if mid + 1 <= len(A) - 1 else float("inf")

            # we already occupied mid + 1 elements. So the other array's left half should be half_amount - mid - 1, then
            Bmax = B[half_amount - mid - 2] if half_amount - mid - 2 >= 0 else float("-inf")
            Bmin = B[half_amount - mid - 1] if half_amount - mid - 1 <= len(B) - 1 else float("inf")

            # check if left portion of small array's max value is smaller
            # than the min value of the right portion of the big array
            if Amax <= Bmin and Bmax <= Amin:
                if total_amount % 2 == 0:  # even
                    return (max(Amax, Bmax) + min(Amin, Bmin)) / 2
                else:
                    return min(Amin, Bmin)

            if Amax > Bmin:
                r = mid - 1
            if Bmax > Amax:  # need to reduce B array, so take more in array 1
                l = mid + 1


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 3]
    nums2 = [2]

    print(s.findMedianSortedArrays(nums1, nums2))
