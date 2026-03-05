from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Let's say we use the example: candidates = [2,3,6,7], target = 7
        
        Firstly, we should sort candidates, which would take O(k*log(k))
        
        If we include 2, then the remaining target is 5, and we are free
        to use the [2, 3, 6, 7] again

        If we don't include 2, then it would only make sense to only
        include [3, 6, 7] in future combination finds, and the target is
        still 7
        
        Back to the include case, we are back to the same decision, if
        we include 2 again, then the remaining search space is still
        [2, 3, 6, 7] and the target is now 3.

        Then if we select 2 again, the search space is still
        [2, 3, 6, 7], and the target is now 1.

        But then we realize that no remaining possible choice. So this
        is not a valid path and we don't need to search further.

        So the tree structure is such that at each node, we can decide
        whether we want to include the currently available candidates.
        And if we choose not to include, we will need to take out this
        current candidate when passing the candidates list to future
        nodes. And if we do include it, then all candidates still remain
        without change.

        The node termination condition is that if the remaining target
        is already smaller than the smallest candidate, or if target
        has reduced to 0, which means a match is found and we append
        the result to the final list.
        """
        res = []
        return res
