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
        the adjacent numbers are different. For the right pointer, we
        don't have to do this explicit check. Because once the left has
        already advanced to the next bigger number, we know that we
        must reduce the current sum. So if the right also has
        duplicates, the while loop would decrement it until the curr_sum
        is reduced
        

        Time Complexity: O(n^2)
            The full time complexity is O(nlog(n)) + O(n * n) = O(n^2)

        Space Complexity: O(1)
            No additional memory is used aside from the output answer
        """
        nums.sort()
        answer = []

        for idx, n in enumerate(nums):
            # check if the previous number is the same (and also safe-
            # guard that there is a number to the left), if so skip
            if idx > 0 and n == nums[idx - 1]:
                continue
            complement = -n

            left, right = idx + 1, len(nums) - 1

            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum == complement:
                    answer.append([n, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicates for left pointer
                    # since we already advanced one, check if the
                    # previous left pointer is pointing at the same
                    # number
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # we don't have to check the right for duplicate,
                    # because if we've already advanced the left pointer
                    # the curr sum is now bigger. Then we must drop the
                    # right pointer. But if right pointer is duplicate
                    # the else: right -= 1 would take care of itself
                    
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