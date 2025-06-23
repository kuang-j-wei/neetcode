from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        The character length will always be n * 2

        And at each character, we have a choice of left
        or right bracket

        We can generate this list of all possible string
        combinations, and then validate whether the
        parentheses are valid

        Time Complexity: O(2 ^ (2n))

        Space Complexity: O(2 ^ (2n))
        """
        results = self.generate_all_parentheses_recursive(n)

        final_answer = []
        for result in results:
            if self.parenthese_checker(result):
                final_answer.append(result)

        return final_answer

    def generate_all_parentheses_recursive(self, n, current="", all_combinations=None):
        """
        Generate all possible combinations of parentheses using recursion

        Args:
            n: Half the length of the string (so total length is 2n)
            current: Current string being built (used in recursion)
            all_combinations: List to store all combinations (used in recursion)

        Returns:
            List of all possible parentheses combinations
        """
        if all_combinations is None:
            all_combinations = []

        # Base case: if we've reached the target length
        if len(current) == 2 * n:
            all_combinations.append(current)
            return all_combinations

        # Recursive case: try adding '(' and ')'
        self.generate_all_parentheses_recursive(n, current + '(', all_combinations)
        self.generate_all_parentheses_recursive(n, current + ')', all_combinations)

        return all_combinations

    def parenthese_checker(self, input_string):
        stack = []

        for char in input_string:
            if len(stack) > 0 and char == ')' and stack[-1] == '(':
                _ = stack.pop()
            else:
                stack.append(char)
        if stack:
            return None
        else:
            return input_string