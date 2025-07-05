class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # if you want to be  greeter, then the leading
        # digit should be larger
        # since we have the same amount of digits, we
        # will have the same order of magnitude
        # the largest integer with the same digits
        # would just be a sorted list of these digits
        # ordered in a descending order
        # but we want the smallest
        # 1197 -> 7119
        # 1234 -> 1243
        # 389274
        # 389724
        # i'm searching near the end of the digits, in order to find a
        # digit that is larger
        # so I'm starting a window from the end of size two, if a digit
        # to the right is bigger, then I will swap it forward, and that
        # is the answer

        digits = [c for c in str(n)]
        length = len(digits)
        stack = [digits[-1]]

        for i in range(length - 2, -1, -1):
            digit = digits[i]

            if digit < stack[-1]:
                # a previously seen digit is bigger, we can swap now,
                # and leave the rest of the digits ordering before
                # this index the same. But we now also have to make sure
                # the rest of the backward counted digits are ordered
                # from the smallest digit to the largest digit
                # so really we could just order
                big_digit = stack.pop()
                stack.append(digit)
                stack.append(big_digit)
                # stack is reverse ordering

                digits = digits[:i]
                digits.extend(stack[::-1])
                return int("".join(digits))
            else:
                stack.append(digit)
        return -1

if __name__ == '__main__':
    s = Solution()
    n = 230241
    s.nextGreaterElement()