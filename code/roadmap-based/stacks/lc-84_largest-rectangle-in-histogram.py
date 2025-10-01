from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Keep a stack of indices, and only stop to calculate area if we
        encounter a bar that's shorter than the current top of the
        stack. Once such bar is encountered, we then count backwards
        in the stack until the current top of the stack is shorter than
        the right limiting wall, we then successfully calculated a
        rectangle.
        """
        n = len(heights)
        max_area = 0
        minimums = [[]]
        for i in range(n):
            for j in range(i + 1, n + 1):
                width = j - i
                if width == 1:
                    height = heights[i]
                else:
                    height = min(height, heights[j - 1])
                max_area = max(max_area, width * height)
        return max_area