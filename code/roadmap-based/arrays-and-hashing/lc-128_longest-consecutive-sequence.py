from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Solution:
            We do a three steps approach

            On first scan, we collect all the unique numbers in the list
            into a hash set

            Then for each number in nums, we check if n - 1 exists. If
            it doesn't exist, we know that it must be a sequence
            beginner, and we save that sequence beginner into another
            hash set

            Then lastly, we just start counting up using each sequence
            beginner. We count up as we check whether n+1 exists

            ---

            Alternatively, we could do the forward counting pass all
            in one go instead of creating a sequence_beginner set.

            We simply iterate over the nums list, and check if n - 1 is
            in nums_hash. If not, we know a sequence beginner has been
            encountered so we can count forward.

            This looks like a O(n^2) nested loop, but that's not the
            actual time cost. Because if a true sequence beginner is not
            encountered, we would never enter the while loop

            And for a non-sequence starter, we would only count it once
            in the while loop

            So at the end each num is only encountered once

        Time Complexity: O(n)
            Constructing the first unique num hash will take O(n)
            as we need to iterate over nums

            Then to create a set of sequence beginners, we again iterate
            over nums and for each num, we check whether there is a
            number smaller than it available via the nums_hash, each
            check being an O(1) operation

            Then lastly, we use the set beginner to count forward. Again
            this would at most make us iterate through all numbers in
            the list nums again so at most can take O(n)

        Space Complexity: O(n)
            We have to save two additional hash sets, which could each
            be at most O(n)

        """
        nums_hash = set(nums)
        max_length = len(nums_hash)

        if max_length == 1:
            return 1
        elif max_length == 0:
            return 0

        # sequence_beginner = set()

        # for n in nums_hash:
        #     if n - 1 not in nums_hash:
        #         sequence_beginner.add(n)

        # max_ans = 1
        # for n in sequence_beginner:
        #     ans = 1
        #     while n + 1 in nums_hash:
        #         ans += 1
        #         n += 1
        #     max_ans = max(max_ans, ans)

        max_ans = 1
        for n in nums:
            if n - 1 not in nums_hash:
                ans = 1
                while n + 1 in nums_hash:
                    ans += 1
                    n += 1
                max_ans = max(max_ans, ans)
        return max_ans