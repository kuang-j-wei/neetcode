from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Solution:
            Only when an operator is encountered, would we need two
            numbers to operate on.

            So we use a stack to save the numbers, because... TBC

        Time Complexity: O(n)
            We only loop through tokens once

        Space Complexity: O(n)
            At worst we would need to store all numbers before operands
            are encountered, so this would take up an additional O(n)
            space for the stack storing numbers
        """
        number_stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                back = number_stack.pop()
                front = number_stack.pop()
                if token == '+':
                    ans = front + back
                if token == '-':
                    ans = front - back
                if token == '*':
                    ans = front * back
                if token == '/':
                    ans = int(front / back)
                number_stack.append(ans)
            else:
                number_stack.append(int(token))
        return number_stack[-1]


if __name__ == '__main__':
    s = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    s.evalRPN(tokens)