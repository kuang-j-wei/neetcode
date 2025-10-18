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

        Now call the smaller (or equal length) array A, the other B.

        Now, regardless of whether the total length of the two arrays
        adds up to even or odd, we are will need (total_length) // 2
        elements in the left partition. So we will take the array that's
        smaller and first find its mid point and take the start to this
        midpoint (inclusive) as the left partition of A. We then just
        need to take `half_length - (midpoint - 1)` amount of elements
        from array B, which together would then form half_length.

        We can then check the max and min value of these 4 sub
        partitions to see if the median condition is met. If it is, then
        for the even total length condition, the answer will be an
        average of the last element of the left partition and the first
        element of the right partition. The last element of the left
        partition is simply max(leftA, leftB), and the first element of
        the right partition is min(rightA, rightB). And if the total
        length is odd, then we now that the way we've set up our
        condition, the right partition will always be one element larger
        than the left partition, because we forced the left partition to
        be of length (total_length // 2), which rounds down. Thus we
        just need to take the first element of the right partition,
        which is min(rightA, rightB).

        Note that as we are doing binary partition on the smaller array,
        there is a chance that left and right pointers would at the edge
        of the array. So then when we try to identify a left partition
        (when mid point is already at -1) that doesn't exist or a right
        partition that doesn't exist (mid point is at len(A)), we can
        resolve this issue by assigning the min value as -inf and max
        value as inf so that we will rely entirely on the other array
        to check if the min max condition has been satisfied. Put
        another way, in conditions like these we know the true median
        lives purely only in the other array therefore the 4 partition
        comparisons will have to be met, and by setting min to -inf and
        max to inf we will make sure that the condition will always be
        met.

        Time Complexity: O(log(n)), n is the smaller length
            We binary search on the smaller array, and once that binary
            search is done the answer is also found, so no need to
            binary search the other array
        Space Complexity: O(1)
            No additional space
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
