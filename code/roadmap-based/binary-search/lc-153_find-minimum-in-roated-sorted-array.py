from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        If it was already sorted, then the element, before it will
        always be smaller, until you hit a number where the element
        before it is not smaller, then you know that you've identified
        the minimum.

        In order words, we need ot find the inflection point.

        We could divide an conquer, and always only search half of the
        array. The key here is to know which half to abandon.

        Once we split into half, we know that for whichever half whose
        last value is the smaller, the minimum value should also be in
        that half. This can be derived from the root case, where
        in the last loop when both halves only have one element, it's
        the one which is the smaller that's the answer.

        Time Complexity: O(log(n))
            Because we keep search half and half of the array, the
            space we need to search through gets logarithmically smaller

        Space Complexity: O(1)
            No additional memory is used
        """
        if len(nums) == 1:
            return nums[0]

        while True:
            n = len(nums)
            mid = n // 2
            first_half = nums[:mid]
            second_half = nums[mid:]

            if len(first_half) == len(second_half) == 1:
                return min(first_half[0], second_half[0])
            elif len(first_half) == 1 and len(second_half) == 0:
                return first_half[0]
            elif len(second_half) == 1 and len(first_half) == 0:
                return second_half[0]

            elif first_half[-1] <= second_half[-1]:
                nums = nums[:mid]
            else:
                nums = nums[mid:]


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    print(f"Answer = {s.findMin(nums)}")
