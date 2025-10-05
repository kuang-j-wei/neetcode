from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Two pass

        First pass find the inflection point

        Then second pass binary search in the correct half of the sorted
        array

        Time Complexity: O(log(n))
            It's two passes of O(log(n))
        Space Complexity: O(1)
            No additional memory is used
        """
        def binary_search(nums, target):
            l, r = 0, len(nums) - 1
            while (r - l) > 1:
                mid = (r - l + 1) // 2 + l
                if target == nums[mid]:
                    return mid
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            if target == nums[l]:
                return l
            elif target == nums[r]:
                return r
            else:
                return -1
            
        if len(nums) == 1:
            return -1 if nums[0] != target else 0
        
        # find inflection point
        l, r = 0, len(nums) - 1
        print(f"(l, r) = ({l}, {r})")
        
        while (r - l) > 1:
            mid = (r - l + 1) // 2 + l
            print(f"mid = {mid}")
            if nums[mid - 1] < nums[r]:  # left is smaller
                r = mid - 1
                print(f"updated r to {r}")
            else:
                l = mid
                print(f"updated l to {l}")
        
        inflection = l if nums[l] < nums[r] else r
        print(f"inflection_point = nums[{inflection}] = {nums[inflection]}")

        # then check if target would be to the left or to the right
        if target <= nums[-1] and target >= nums[inflection]:
            nums = nums[inflection:]
            print(f"feeding {nums} into binary_search")
            ans = binary_search(nums, target)
            print(f"Target found at = {ans}")
            return -1 if ans == -1 else ans + inflection
        else:
            nums = nums[:inflection + 1]
            print(f"feeding {nums} into binary_search")
            ans = binary_search(nums, target)
            print(f"Target found at = {ans}")
            return -1 if ans == -1 else ans
        

if __name__ == '__main__':
    s = Solution()
    # nums = [3, 4, 5, 6, 1, 2]
    # nums = [3, 5, 6, 0, 1, 2]
    nums = [1, 3]
    # target = 4
    target = 0

    s.search(nums, target)
