from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        We iterate forward, and keep adding bars to a stack, until we
        see a bar that's shorter than the most recent bar, which would
        be the top of the stack.

        Then we know that we have to count backwards, 
        We will keep a stack of indices, where each index essentially
        stores 'the index of the left wall'
        """
        max_area = 0
        stack = []

        for i, curr_height in enumerate(heights):
            start = i
            while stack and curr_height < heights[stack[-1]]:  # can't extend to the right anymore, look back to the left
                lookback_index = stack.pop()
                limiting_height = heights[lookback_index]
                width = i - lookback_index
                max_area = max(max_area, width * limiting_height)
                start = i
            stack.append(start)

        for index in stack:
            max_area = max(max_area, heights[index] * (len(heights) - index))
            
        return max_area