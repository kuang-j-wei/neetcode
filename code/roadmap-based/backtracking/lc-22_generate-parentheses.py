from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Space Complexity: O(n)
            O(n) possible recursive stacks for the depth of the tree
            And also O(n) for the `curr_str` list
        """
        result = []
        curr_str = []

        def backtrack(right_count, left_count):
            if right_count == left_count == n:
                result.append("".join(curr_str))  # this join will be O(2n)
                return None
            if right_count > left_count:
                curr_str.append(')')
                backtrack(right_count, left_count + 1)
                curr_str.pop()
            if right_count < n:
                curr_str.append('(')
                backtrack(right_count + 1, left_count)
                curr_str.pop()

        backtrack(0, 0)
        return result