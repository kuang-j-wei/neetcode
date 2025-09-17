from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        We want to maximize width and height

        Brute force would be, iterate through the array, and at
        each step would be min(height[i], height[j]) * (j - i)

        This would be an O(n^2) solution.

        If we start with two pointers, one from the left one
        from the right. Then the area would be
        min(height[i], height[j]) * (j - i)

        Then if we want to increase this, we will have to increase
        min(height[i], height[j]), at a cost of decreasing (j - i),
        which is the width

        We can just step by step search this potential maximum. To
        maximize the height, we will just change the pointer that's
        pointing to the shortest height, because then this is the only
        way we could feasibly get an increase in the area. And we will
        just calculate the current area and only update the maximum
        area if the current area is bigger

        Time Complexity: O(n)
            With this two pointer approach we will terminate the while
            loop when the two pointers overlap. So we at most we only
            iterate over the array once
        
        Space Complexity: O(1)
            We don't require additional memory
        """
        left, right = 0, len(height) - 1
        curr_area = min(height[left], height[right]) * (right - left)
        max_area = curr_area

        while left < right:
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            
            curr_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, curr_area)
        return max_area