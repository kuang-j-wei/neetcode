from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        We iterate forward, and keep adding bars to a stack, until we
        see a bar that's shorter than the most recent bar, which would
        be the top of the stack. In this approach, the stack will always
        be in an increasing order.

        Once a shorter bar is encountered, we know that the current
        tallest bar can't be extend to the right anymore, so we can
        start counting the area that iit can occupy. And the area it can
        occupy is its own height, to the current pointer right boundary.

        As we are going backwards (popping the stack), once we find a
        bar that's shorter or the same height as the limiting height,
        then we know that we can stop, because this is now a bar that
        can be extended to the right. We also note this current left
        pointer as the "index" of this bar that's getting added to the
        stack. Because this represent how far back this right wall can
        be extended to.

        Once we've reached the end of the input array, if we have
        elements left in the stack, we just need to calculate their
        area by limiting height to width, which is the recorded left
        pointer to the full length of the array

        Time Complexity: O(n)
            Each element is pushed and popped once into and from the
            stack only once

        Space Complexity: O(n)
            The stack can at most grow to the same size as the input
            array


        """
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            limiting_index = i
            while stack and h < stack[-1][1]:  # can't extend to the right anymore, look back to the left
                limiting_index, limiting_height = stack.pop()
                width = i - limiting_index
                max_area = max(max_area, limiting_height * width)
            stack.append((limiting_index, h))

        # forward pass
        n = len(heights)
        while stack:
            idx, h = stack.pop()
            width = n - idx
            max_area = max(max_area, h * width)
        return max_area
