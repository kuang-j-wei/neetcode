from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Need to find a method to take care of,
        spilled out, but there are sub-problems we can
        solve
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
            else:  # left shorter, spill out
                current_water = 0


        return water_sum