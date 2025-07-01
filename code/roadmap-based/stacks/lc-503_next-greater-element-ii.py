from typping import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        Solution:
            The next greater number would only not exist
            if a number is truly the maximum

            This would only happen if you've succesfully
            looped once and didn't find any larger number

            So we can just double the size of nums and
            loop through it once to find the next larger
            number

        Time Complexity: O(n)
            We sitll only loop through nums once at double
            its size

        Space Complexity: O(n)
            The stack itself may grow to the size of nums
        """


        stack = []
        nums = nums * 2
        answer = [-1] * len(nums)

        for idx, n in enumerate(nums):
            while stack and n > stack[-1][-1]:
                answer[stack[-1][0]] = n
                stack.pop()

            stack.append((idx, n))

        return answer[:(len(nums) // 2)]