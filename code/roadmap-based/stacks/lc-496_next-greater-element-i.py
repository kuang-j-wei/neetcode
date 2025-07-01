class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Solution:
            Need a map to tell you what value in nums2 has next greater
            num and what that num is

            We then simply loop through nums1 and use the lookup to see
            what the curr num's next greater number is. If it doesn't
            exist, then the answer is -1

            As to how to find the next greater number, we keep a stack
            of the most recent numbers (last in first out), and whenever
            we see that the curr number is larger than the top most of
            the stack, we know that the next greater number has been
            found and we will keep checking backwards in the stack by
            popping out the top most value

            When the stack is empty or no smaller number has been found,
            then we know we have hit a new small number and we add it
            into the stack

        Time Complexity: O(n)
            Since we are iterating over nums1 and nums1 each once only

        Space Complexity: O(n)
            The additional map to store the next greater number can
            take up a full length as nums2
        """
        stack = []
        lookup = {}
        answer = []
        for num in nums2:
            # iterate forward on each number and save
            # the most recent value
            # if the current value is larger than the
            # most recent value, then record down
            # this number, and then further go check
            # the stack backwards to see if the number
            # is also lower
            while stack and num > stack[-1]:
                lookup[stack[-1]] = num
                stack.pop()
            # either stack is empty or we've hit a number
            # that's bigger in our backward count
            # add it to our stack
            stack.append(num)

        for n in nums1:
            if n not in lookup:
                answer.append(-1)
            else:
                answer.append(lookup[n])
        return answer