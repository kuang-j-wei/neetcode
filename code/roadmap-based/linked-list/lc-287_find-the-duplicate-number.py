from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Use the array value itself as a reference index, and use this
        index to get the next value. So for example, the first position
        is of value "1", then we reference the nums[1] as the next
        node's value. And then we can use the value of nums[1] as the
        index to reference the next value.
        """
        # for i, ni in enumerate(nums):
        #     for j, nj in enumerate(nums[i + 1:]):
        #         if ni == nj:
        #             return ni

        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow 
