from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Trivial solution would just be O(n) because we can just search
        through `nums` and return the matched number

        But because it's sorted, we could search the target in a binary
        search way to achieve O(log(n))

        But now we have to take care of the fact that it's rotated,
        which makes which half to choose tricky
        """
        return None
