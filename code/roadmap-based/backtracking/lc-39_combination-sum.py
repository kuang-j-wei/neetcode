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
        nodes. To save on space, we can just pass indices of
        `candidates` to limit the usable candidates. And if we do
        include it, then all candidates still remain without change.

        The node termination condition is that if the remaining target
        is already smaller than the smallest candidate, or if target
        has reduced to 0, which means a match is found and we append
        the result to the final list.

        Time Complexity: O(2^(target / m)) 
            The time complexity would depend on how many nodes we have
            in this binary tree. At each layer we could at worst be
            doubling the number of nodes from the current layer to the
            next layer. The depth of the tree is bounded by the case
            where we accept the minimum candidate, and keep doing so
            until we've exceeded a sum that's larger than the target.
            Therefore if the minimum value of candidates is `m`, then
            the maximum depth of the tree is `target / m`. And again at
            each layer we are at worst doubling the number of nodes, so
            the total time complexity is O(2 ^(target / m))
            
        Space Complexity: O((target/m) ^ 2)
            The height of the binary tree is `(target / m)` as argued
            in the above Time Complexity analysis. Further, as we are
            doing `running_list + [lowest_candidate]`, this creates a
            new list, so we could at worst be copying a list that's as
            long as the maximum depth, which again is `(target / m)`.
            So each new frame needs to hold a new copy of the current
            `running_list`. And this `running_list` grows the deeper you
            go into the tree depth, at each depth increasing the length
            of the `running_list` by one, where at the deepest the total
            length is (target / m). So the total memory the function
            needs to hold at a time at worst is `1 + 2 + 3 + ... +
            target / m`, which sums to (1/2 * t/m * (t/m + 1)) which
            is roughly O((t/m)^2)
        """
        candidates.sort()
        self.candidates = candidates
        self.res = []
        self.dfs([], 0, target)
        return self.res
    
    def dfs(self, running_list, candidates_idx, remaining_target):
        # already out of bound of target is too small, quit
        if candidates_idx >= len(self.candidates) or remaining_target < 0:
            return None
        
        lowest_candidate = self.candidates[candidates_idx]
        
        # out of possible candidate, quit
        if lowest_candidate > remaining_target:
            return None
        
        # direct math, append, then quit
        if lowest_candidate == remaining_target:
            self.res.append(running_list + [lowest_candidate])
            return None
        
        # otherwise, continue to bifurcate
        # we either include this current node or not
        self.dfs(running_list, candidates_idx + 1, remaining_target)
        self.dfs(running_list + [lowest_candidate], candidates_idx, remaining_target - lowest_candidate)
