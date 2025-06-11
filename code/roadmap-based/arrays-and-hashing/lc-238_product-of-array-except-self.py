from typing import List

class SolutionOptimal:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Solution:
            Let prefix[i] be all the nums multiplied together up to
            right before this i-th position

            And if there's no num in front, initialize ias 1

            Let suffix[j] be all the nums multiplied starting from the
            back together up to right after this index

            Then ans[i] will just be prefix[i] * suffix[i]

            We can first store prefix in the ans array itself

            Then we store a suffix variable, which starts from 1 and
            then we gradually multiply up by each num that we are
            iterating on

            Then when we do a second backward pass, we just multiply
            ans[j] with this current running suffix


            nums   = [1, 2, 3, 4]

            prefix = [1] + [1, 2, 6]
            suffix = [24, 12, 4] + [1]
        
        Time Complexity: O(n)
            Because we linearly run two loops each of length len(nums)

        Space Complexity: O(1)
            Technically O(n) because the output array will be the same
            length as the input nums array, but there's no additional
            space needed so O(1)

        """
        length = len(nums)

        answer = [1] * length

        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]

        suffix = 1
        for j in range(length - 2, -1, -1):
            suffix *= nums[j + 1]
            answer[j] = answer[j] * suffix

        return answer


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Solution:
            ans[0] =      1  * nums[1] * nums[2] * nums[3]
            ans[1] = nums[0] *      1  * nums[2] * nums[3]
            ans[2] = nums[0] * nums[1] *      1  * nums[3]
            ans[3] = nums[0] * nums[1] * nums[2] *      1

            So we can decompose this into prefix * suffix

            Let
            prefix[0] = 1
            prefix[1] = 1 * nums[0] = prefix[0] * nums[0]
            prefix[2] = 1 * nums[0] * nums[1] = prefix[1] * nums[1]
            prefix[i] = prefix[i - 1] * nums[i - 1]

            Let
            suffix[4] = 1
            suffix[3] = nums[3] * suffix[4] = nums[3] * 1
            suffix[2] = nums[2] * suffix[3] = nums[2] * nums[3] * 1
            suffix[1] = nums[1] * suffix[2] = nums[1] * nums[2] * nums[3] * 1
            suffix[0] = nums[0] * suffix[1] = nums[0] * nums[1] * nums[2] * nums[3] * 1
            suffix[i] = nums[i] & suffix[i + 1]

            Then ans[i] = prefix[i] * suffix[i + 1]

        Time Complexity: O(n)
            Because we just linearly process nums three times

        Space Complexity: O(n)
            Because prefix and suffix have to each occupy O(n)

        """
        length = len(nums)
        answer = [0] * length
        prefix = [1] * (length + 1)
        suffix = [1] * (length + 1)

        for i in range(1, length + 1):
            # 1 to 4  # index of prefix, forward processing
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # suffix has to be filled from back to front because we are
        # multiplying from the end of nums to forward, with the very
        # last element being 1 to handle the first multiplication
        # being the num itself
        for j in range(length - 1, -1, -1):
            suffix[j] = nums[j] * suffix[j + 1]

        for i in range(length):
            answer[i] = prefix[i] * suffix[i + 1]
        return answer


class SolutionBruteForce:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Solution:
            Brute force would be an O(n^2) solution, as we simply nested
            loop multiply all possible combinations

        """
        answer = [0] * len(nums)

        for i in range(len(nums)):
            ans = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    ans *= nums[j]
            answer[i] = ans
        return answer