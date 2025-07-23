from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Solution:
            At each number, we can check the complement to the target
            
            We also add thiis number to a dictionary, keyed by value
            and valued by index

            If it doesn't exist, then we add the current element to
            the dictionary. If it does exist, return the keyed index
            and the current index

            But the solution asked for constant extra space, and the
            the array is already in a descending order. Then for each
            complement, we can search to the mid between current
            number annd the end of the number. If the complement needed
            is larger than the mid number, then we search higher.
            
            This divide approach makes the time compleixty of each searh
            only O(log(n))

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
    numbers = [1,2,3,4,4,9,56,90]
    
    s = Solution()

    s.twoSum(numbers, target)