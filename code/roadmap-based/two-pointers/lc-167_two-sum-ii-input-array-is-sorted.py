from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Solution:
            Since we know that a solution always exists and that the
            array is sorted, we can "close in" on the two ends

            We can achieve this by simply summing the numbers from the
            two ends. And if the sum is greater than the target, then
            we know that we must decrease this sum. And the only way
            to achieve that is to bring the end pointer a position to
            the left.

            And if now the sum is too small, then we know that we need
            to advance the left pointer

            We do this until an answer is found

        Time Complexity: O(n)
            We only make one pass to the array
        
        Space Complexity: O(1)
            No additional space is needed
        """
        left = 0
        right = len(numbers) - 1

        while True:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return (left + 1, right + 1)
            if curr_sum > target:
                right -= 1
            else:
                left += 1


class SolutionBinarySearch:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Solution:
            At each number, we can check the complement to the target
            
            We also add this number to a dictionary, keyed by value
            and valued by index

            If it doesn't exist, then we add the current element to
            the dictionary. If it does exist, return the keyed index
            and the current index

            But the solution asked for constant extra space, and the
            the array is already in a descending order. Then for each
            complement, we can search to the mid between current
            number and the end of the number. If the complement needed
            is larger than the mid number, then we search higher.
            
            This divide approach makes the time complexity of each
            search only O(log(n))

        Time Complexity: O(n long(n))

        Space Complexity:: O(1)
        """
        n = len(numbers)
        for i in range(n - 1):
            num = numbers[i]
            complement = target - num

            left = i + 1
            right = n - 1
            while left <= right:
                mid = (left + right) // 2
                new_num = numbers[mid]
                if new_num == complement:
                    return [i + 1, mid + 1]
                else:
                    if complement > new_num:
                        left = mid + 1
                    else:
                        right = mid - 1


if __name__ == '__main__':
    target = 8
    # numbers = [1,2,3,4,4,9,56,90]
    numbers = [12,13,23,28,43,44,59,60,61,68,70,86,88,92,124,125,136,168,173,173,180,199,212,221,227,230,277,282,306,314,316,321,325,328,336,337,363,365,368,370,370,371,375,384,387,394,400,404,414,422,422,427,430,435,457,493,506,527,531,538,541,546,568,583,585,587,650,652,677,691,730,737,740,751,755,764,778,783,785,789,794,803,809,815,847,858,863,863,874,887,896,916,920,926,927,930,933,957,981,997]
    
    s = Solution()

    print(s.twoSum(numbers, target))