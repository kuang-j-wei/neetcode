class Solution:
    def nextGreaterElement(self, n: int) -> int:
        """
        Solution:
            We want to start from the back and start scanning. If we
            find a new digit in the front that's smaller than any of the
            previously seen digit, then we know that we need to swap
            a digit in the back to the front

            We do so by utilizing a stack. If the last position of the
            stack is smaller than this newly scanned digit, then we
            append it this new digit. This way the stack is ensured to
            be in ann increasing order

            Then the moment we see that a new digit is smaller than the
            last position, we know that we now have a old digit that's
            larger than this new digit

            But we don't always want to move this old largest digit to
            the front. We just want a old digit that's larger than this
            current digit to move to the front

            So we again start iterating through the stack but from the
            front. If the new stack number is smaller than the current
            digit, skip. If it's larger, then we have found the
            candidate to swap with digit. So we append this candidate.

            Then the rest of the digits should be what we have
            previously scanned from the back, but we want it to be in
            increasing order, and we have to add in this digit acquired
            from digits. But since the stack is already guaranteed to be
            in increasing order, and we already one by one checked from
            the front of the stack that each number is smaller than
            digit. Then we know we can just "insert" digit at the middle
            and the stack will just be in increasing order

        Time Complexity: O(n)
            Because we are only scanning through digits. And even in
            that inner loop, we won't iterate anything that's over the
            length of n and the function will terminate there
        
        Space Complexity: O(n)
            At worst we would keep a stack that's the same length as the
            input array
        """
        digits = [c for c in str(n)]
        length = len(digits)
        stack = [digits[-1]]

        for i in range(length - 2, -1, -1):
            digit = digits[i]

            if digit < stack[-1]:
                # finally a smaller number is found
                # first save the digits in front
                # then we search through the stack and find the smallest 
                # number in the stack that's larger than this current
                # And since the stack is already ensured to be in an
                # ascending order, we know that we can then just insert
                # digit at this point and it's 
                digits = digits[:i]
                for j in range(len(stack)):
                    if stack[j] > digit:
                        digits.append(stack[j])
                        stack = stack[:j] + [digit] + stack[j+1:]
                        stack.sort()
                        digits.extend(stack)
                        ans = int("".join(digits))
                        return ans if ans <= (2 ** 31 - 1) else -1
                return ans 
            else:
                stack.append(digit)  # we will be in increasing order
        return -1

if __name__ == '__main__':
    s = Solution()
    n = 2147483476
    print(s.nextGreaterElement(n))