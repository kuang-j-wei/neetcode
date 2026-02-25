from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        We need to find every combination possible.

        The power set will include sub-lists with length ranging from 0
        to n

        And at each length, i, we can will fill digits with enough yes
        until this current sublist is full. 
        """
        self.res = []

        # loop through including 1, including 2, including 3, ...

        self.dfs(nums)
        
        return self.res
    
    def dfs(nums):
        if not nums:
            return self.res.append([])
        if len(nums) == 1:
            return self.res.append(nums)

        for n in nums:
            pass
