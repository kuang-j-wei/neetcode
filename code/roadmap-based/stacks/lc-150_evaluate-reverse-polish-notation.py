from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Solution:
            For the reverse Polish notation, because the operators
            are after numbers, we iterate until we see an operator. Then
            once we encounter an operator, we know need to look
            backwards of the two most recent numbers seen.

            So this is a Last In First Out processing order, which is
            suitable for a stack.

            And once the new number is calculated based on that
            operator, it becomes the latest number that could be
            operated on, so we put it into the stack.

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