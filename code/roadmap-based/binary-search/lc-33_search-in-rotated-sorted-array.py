from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        We will perform a binary search to achieve O(log(n)) time, and
        the key here again is to know which half to preserve.

        The key insight here is that, if we conceptualize the array as
        elements to the left of the inflection point as the "left
        portion" and to the right (inclusive of inflection) as the
        right, then we can use this to determine which  half to keep.

        Now if we are in the left half, and the target is smaller than
        the midpoint, then we know to binary search left to midpoint.

        If we are in the left half, and the target is larger than
        the mid point, we will search from the midpoint forward to the
        inflection point. But we don't know where the inflection point
        is, so we will just search from the midpoint + 1 to the end.

        If we are in the right half, and the target is larger than the
        mid point, then we search from midpoint to the end of the array.

        If we are in the right half and the target is less than the mid
        point, then we search from inflection point to the mid point.
        But again we don't know the inflection point, so we will just
        search from left pointer to midpoint - 1.

        Now to determine whether we are in the left portion or the right
        portion - We know that in the left portion, its left most
        element is smaller than all elements in the left portion. But
        the left most element is bigger than all elements of the right
        portion. So if the mid pointer is larger than the left pointer,
        then we know we are in the left portion. If it's smaller than
        the left pointer, then we know we are in the right portion.

        And to determine portion the only important thing is that we
        have to make sure we are in an ascending order.
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
        """
        We will perform a binary search to achieve O(log(n)) time, and
        the key here again is to know which half to preserve.

        The key insight here is that, if we conceptualize the array as
        elements to the left of the inflection point as the "left
        portion" and to the right (inclusive of inflection) as the
        right, then we can use this to determine which  half to keep.

        Now if we are in the left half, and the target is smaller than
        the midpoint, then we know to binary search left to midpoint.

        If we are in the left half, and the target is larger than
        the mid point, we will search from the midpoint forward to the
        inflection point. But we don't know where the inflection point
        is, so we will just search from the midpoint + 1 to the end.

        If we are in the right half, and the target is larger than the
        mid point, then we search from midpoint to the end of the array.

        If we are in the right half and the target is less than the mid
        point, then we search from inflection point to the mid point.
        But again we don't know the inflection point, so we will just
        search from left pointer to midpoint - 1.

        Now to determine whether we are in the left portion or the right
        portion - We know that in the left portion, its left most
        element is smaller than all elements in the left portion. But
        the left most element is bigger than all elements of the right
        portion. So if the mid pointer is larger than the left pointer,
        then we know we are in the left portion. If it's smaller than
        the left pointer, then we know we are in the right portion.

        And to determine portion the only important thing is that we
        have to make sure we are in an ascending order.
        """
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
    nums = [1, 3]
    # target = 4
    target = 0

    s.search(nums, target)
