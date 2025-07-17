from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                width = j - i
                height = min(heights[i:j])
                max_area = max(max_area, width * height)
        return max_area