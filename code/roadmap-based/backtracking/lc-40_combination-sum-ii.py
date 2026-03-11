class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        We could use the same approach as LeetCode 40 Combination. It's
        a bit simplified as at each depth, the available candidates is
        the same

        But because we can't have the same combinations of digits
        repeating in the final answer, we will also need to use a
        hashmap to perform deduping. At a basic level, we can keep the
        results as a set. And when the running target reaches zero,
        meaning we have found an exact match, we can check against the
        overall set to see if this list already exists. And because we
        already sorted `candidates`, the running_list will always
        already be ordered and therefore using a set to check whether
        we have already seen a list, will allow us to always match up
        to a combination that have already existed.

        But this fails for a repeated input of 100 1's with a target=30.
        So the smarter approach would be to turn the candidates into
        a dictionary keyed by the unique values of candidates and valued
        by their frequencies. And if an answer uses the same unique
        values, it's a repeated.

        But a new hint suggests to use the sorted array and adjacent
        same numbers to prevent the same combinations for from being
        explored multiple times.
        """
        self.res = set()
        self.candidates = candidates
        self.candidates.sort()

        running_list = []
        self.dfs(running_list, 0, target)

        self.res = [list(r) for r in self.res]
        return self.res

    def dfs(self, running_list, candidate_start, running_target):
        if candidate_start >= len(self.candidates):
            return None
        candidate = self.candidates[candidate_start]
        if candidate > running_target or running_target < 0:
            return None
        if candidate == running_target:
            possible_answer = tuple(running_list + [candidate])
            if possible_answer not in self.res:
                self.res.add(possible_answer)
            return None
        
        # traverse
        self.dfs(running_list + [candidate], candidate_start + 1, running_target - candidate)
        self.dfs(running_list, candidate_start + 1, running_target)
