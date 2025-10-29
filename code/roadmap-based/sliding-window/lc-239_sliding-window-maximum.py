from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        First iterate through `nums` until the size of k, and as we
        iterate, record down the maximum number. We will do so by
        keeping a left pointer which starts at 0 and a r pointer which
        will eventually reach r - l + 1 = k

        Then if the current left pointer is the max, right before we
        increment l, we compare this current l with the incremented r
        to see which one is bigger. If l is not the max, then we just
        compare the new r value with the current max to see which one
        is bigger. But if l is the biggest, we would then need to find
        the next biggest number. We could just then search through the
        newly slid window to find the maximum.
        """
        maxes = []

        l, r = 0, k
        print(f"Finding max({nums[l:r]})")
        maxes.append(max(nums[l:r]))
        print(f"maxes = {maxes}")

        while r < len(nums):
            if maxes[-1] != nums[l]:
                print(f"Appending max(nums[{r}], maxes{-1}) = max({nums[r]}, {maxes[-1]})")
                maxes.append(max(nums[r], maxes[-1]))
                print(f"maxes = {maxes}")
            else:
                print(f"Appending max({nums[l + 1:r + 1]})")
                maxes.append(max(nums[l + 1:r + 1]))
                print(f"maxes = {maxes}")
            l += 1
            r += 1
        return maxes


if __name__ == '__main__':
    s = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3

    s.maxSlidingWindow(nums, k)
