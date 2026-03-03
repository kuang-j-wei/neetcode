from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        We can iterate though each element of nums, and at each element
        we make a decision on yes/no of whether we include this element
        in a subset. This forms a binary decision tree of depth n, and
        at each layer we double the number of nodes. Then a subset is
        formed when we reach a leaf node, and at this point we can add
        that sublist to the power set.
        
        Time Complexity: O(n * 2^n)
            For each digit we have a yes/no decision, which depends on
            the length of a sublist, would then take 2^n combinations.
            Then each sublist can contain up to n elements, 
        
        Space Complexity: O(n * 2^n)
            The recursive stack would build up to a depth of O(n). But
            we are also passing `sublist` to each of the recursive dfs
            call, and each of the sublist could at most build up to the
            length of O(n), and in the last layer, there are O(2^n)
            nodes, each with a sublist that's of length n, so the total
            space complexity is of O(n * 2^n)
        """
        self.res = []
        self.nums = nums

        self.dfs(0, [])
        
        return self.res
    
    def dfs(self, idx, sublist):
        if idx >= len(self.nums):
            self.res.append(sublist)
            return None
        curr = self.nums[idx]
        self.dfs(idx + 1, sublist + [curr])
        self.dfs(idx + 1, sublist)
        return None
