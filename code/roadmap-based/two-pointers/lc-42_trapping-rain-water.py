from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
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