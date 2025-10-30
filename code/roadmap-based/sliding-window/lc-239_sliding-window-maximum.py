from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        We will keep a monotonically decreasing queue as we slide
        through nums. Then we will always be able to access the current
        largest number in the window in O(1) time. And whenever we need
        to add a new number, and this new number is larger than anything
        in the queue, we will pop out the smaller number in the queue
        then add this new number, so this queue is always in a
        monotonically decreasing order. And if the oldest element in
        this queue is now too far away from the current index that means
        the window is too big, so we pop from the left to remove the
        oldest element to decrease the window size.

        Time Complexity: O(n)
            We only visit each element in nums at most twice
        
        Space Complexity: O(k)
            The queue is at most size k
        """
        queue = deque([])
        maxes = []

        for idx, num in enumerate(nums):            
            # if the current window is going to be too big, then we
            # slide out the left most, oldest, indices in the queue
            while queue and (idx - queue[0] + 1) > k:
                queue.popleft()
            
            # for new joiner, remove 
            while queue and num > nums[queue[-1]] :
                queue.pop()
            queue.append(idx)
            
            # window big enough now, we can record
            if idx >= k - 1:
                maxes.append(nums[queue[0]])
                
        return maxes


if __name__ == '__main__':
    s = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3

    s.maxSlidingWindow(nums, k)
