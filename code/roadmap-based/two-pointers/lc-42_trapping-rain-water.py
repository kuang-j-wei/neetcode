from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        We will perform the search in a "two pass" logic

        We use a left and right pointer, and start from the left to the
        end. We keep the left pointer at the "left wall", and at each
        step calculate the potential maximum water we could capture at
        this location, which would be the height of the left wall minus
        the current height. We continue doing so, until we reach a right
        wall that's the same height or taller than the left wall. We can
        then collect the water and then move the left wall to this
        point.

        Now, when we reach the end, the last wall very likely will not
        be the same height or taller than the left wall. But we know
        the current highest wall, which would be the current left wall
        pointer. So we can then perform the same process, but start from
        the end of the array, and go backwards until we hit the highest
        wall. Again we will use a right and left pointer approach, with
        the right pointer starting from the end of the array, and the
        left pointer one position to the left of it. 


        Time: O(n)
            We at most pass the entire array twice (once forward once
            backward)

        Space: O(1)
            No additional memory is used
        """
        if len(height) <= 2:
            return 0

        water_sum = 0
        current_water = 0
        i, j = 0, 1

        while j < len(height):
            if height[i] > height[j]:  # left taller, keep adding volume
                current_water += height[i] - height[j]
                j += 1
            elif height[i] <= height[j]:  # left shorter or equal height, collect water
                water_sum += current_water
                i = j
                j += 1
                current_water = 0

        # end has been reached, we then work backwards to the highest
        # point, which is i
        right = len(height) - 1
        left = right - 1
        current_water = 0

        while left >= i:
            if height[left] >= height[right]: # spill or collect
                water_sum += current_water
                current_water = 0
                right = left
                left = right - 1
            elif height[left] < height[right]: # right taller, add to current
                current_water += height[right] - height[left]
                left -= 1

        return water_sum