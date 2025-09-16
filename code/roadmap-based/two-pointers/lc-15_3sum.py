from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        First sort, then we have sub-problems of sorted Two Sum

        We loop through the numbers, then at each iteration, we search
        through the list to the right as a 2sum sub-problem

        Note that, to avoid duplicates, once a valid triplet is found,
        we should avoid numbers that have already been used. Since this
        is a sorted array, we can now advance the left pointer until
        the adjacent numbers are different. And we do the same for the
        right pointer, decrement it until the numbers are different
        

        Time Complexity: O(n^2)
            The full time complexity is O(nlog(n)) + O(n * n) = O(n^2)

        Space Complexity: O(1)
            No additional memory is used aside from the output answer
        """
        nums.sort()
        length = len(nums)
        answer = []

        for idx1, n1 in enumerate(nums):
            if idx1 - 1 >= 0 and n1 == nums[idx1 - 1]:
                continue
            complement = -n1

            left = idx1 + 1
            right = length - 1

            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum == complement:
                    answer.append([n1, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicates for left pointer
                    # since we already advanced one, check if the
                    # previous left pointer is pointing at the same
                    # number
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicates for right pointer
                    # since we already decrement right by one, check
                    # if one position to the right is the same number
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif curr_sum < complement:
                    left += 1
                else:
                    right -= 1

        return answer


class SolutionDebug:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        answer = []

        print(f"nums = {nums}\n")

        for idx1, n1 in enumerate(nums):
            print(f'Iterating on nums[{idx1}] = {n1}')
            complement = -n1

            left = idx1 + 1
            right = length - 1
            print(f"Searching for complement = {complement} in {nums[left:right]}")

            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum == complement:
                    print(f"Found nums[{left}] = {nums[left]} and nums[{right}] = {nums[right]} that match; appending {[n1, nums[left], nums[right]]}")
                    answer.append([n1, nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif curr_sum < complement:
                    left += 1
                else:
                    right -= 1
            print('')
        return answer


if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    s = Solution()
    print(s.threeSum(nums))