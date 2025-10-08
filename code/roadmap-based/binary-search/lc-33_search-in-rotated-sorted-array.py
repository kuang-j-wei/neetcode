from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        In binary search, we want to know which half to drop. This is
        straight forward in a standard sorted array, we just check if
        the target is bigger or smaller than the mid point, then
        continue until the left and right pointers land on the same
        spot.

        But in this case, we can't guarantee that all elements left of
        the mid point is actually smaller, because if we encounter an
        inflection point, then there will be bigger values even to the
        left of the mid point.

        But a key observation here is that, within the left or right
        portion of the rotated array, the array is a strictly increasing
        sorted array. We can use this to our advantage.

        Let's call all the numbers to the left of the inflection point
        the left portion and all points to the right the right portion.
        One key observation here is that the left most number in the
        left portion is still larger than all numbers in the right
        portion. And the right most value in the right portion is still
        smaller than all values in the left portion.

        If we the mid point is in the left array, and we know that the
        target is bigger than the current mid point, we are guaranteed
        to only need to look to the right of the mid point. But if the
        target is smaller, we either have to look from the current left
        to mid, or we might actually have to look to the "right portion"
        of the array, since the target might be so small that it's
        actually in the right portion. But this is also exactly the key
        insight - by comparing the left most value in the left array
        against target, if target is greater than this left most value,
        then we know we just have to search from left to mid - 1.
        Otherwise, we know that the target could only be in the "right
        portion", so then we would update the left pointer to mid + 1.

        Similar logic applies if the mid point is in the "right
        portion". If target is smaller, then we know we just need to
        search within everything lower than mid point, so update r to
        mid - 1. But if target is bigger, then it's either in the "right
        portion" or it's in the "left portion" altogether. To know this,
        we just compare the right most value to the target. If the right
        most is still bigger than the target, then we just need to
        search in this "right portion". But if it's smaller, then we
        know the target could only be in the "left portion" since all
        numbers in the "left portion" is bigger than even the last
        number int he "right portion". So then we update the right
        pointer to mid - 1 since we just need to search the left portion
        of the array.
        
        
        Time Complexity: O(log(n))
            We are doing a binary search, so at most we can just need
            to do log(n) operations before finding or ruling out the
            existence of target
        
        Space Complexity: O(1)
            No additional space is used
        """
        l, r = 0, len(nums) - 1

        while l <= r:  # need to narrow down to just one element, which is when left overlaps with right, and mid will also be the same point, and we check for target
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[l]:  # we are in left portion
                if nums[mid] < target or target < nums[l]:  # need to look for larger number, so just need to look to the right
                    l = mid + 1
                else:
                    r = mid - 1
            else:  # in right section
                if nums[mid] > target or nums[r] < target:  # need to find smaller value, so look to the left
                    r = mid - 1
                else:
                    l = mid + 1  # it's just this right section
        return -1


class SolutionVerbose:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:  # need to narrow down to just one element, which is when left overlaps with right, and mid will also be the same point, and we check for target
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[l]:  # we are in left portion
                if nums[mid] < target:  # need to look for larger number, so just need to look to the right
                    l = mid + 1
                else:  # need to look for smaller number, so either look to the left or to the right portion
                    if target > nums[l]:  # just need to keep looking to the left
                        r = mid - 1
                    else:  # need to look for the right most portion
                         l = mid + 1
            else:  # in right section
                if nums[mid] > target:  # need to find smaller value, so look to the left
                    r = mid - 1
                else:  # need to find larger value, so look to the right or look for the left most section
                    if nums[r] > target:
                        l = mid + 1  # it's just this right section
                    else:  # need to look into the left section
                        r = mid - 1
        return -1


class SolutionSlow:
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
    # nums = [1, 3]
    nums = [4,5,6,7,0,1,2]
    # target = 4
    target = 0

    s.search(nums, target)
