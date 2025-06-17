from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums_hash = set(nums)
        max_length = len(nums_hash)

        if max_length == 1:
            return 1
        

        ans = 1
        max_ans = 1

        # beginning = min(nums_hash)
        # nums_hash.remove(beginning)

        # while len(nums_hash) > 0:
        #     if beginning + 1 in nums_hash:
        #         # print(f"{beginning} + 1 found in {nums_hash}, incrementing {ans} by 1")
        #         ans += 1
        #         max_ans = max(max_ans, ans)
        #         nums_hash.remove(beginning + 1)
        #         beginning += 1
        #         # print(f"beginning set to {beginning}, nums_hash = {nums_hash}, with ans = {ans}\n")
        #     else:
        #         # print(f"{beginning} + 1 not found in {nums_hash}, setting beginning to {min(nums_hash)} and ans = 1")
        #         beginning = min(nums_hash)
        #         nums_hash.remove(beginning)
        #         max_ans = max(max_ans, ans)
        #         ans = 1
        # return max_ans
            

        for n in nums:
            # print(f"Starting a new search for {n}, current ans = {ans}")
            ans = 1
            head = n
            tail = n
            while ans < max_length:
                if head + 1 in nums_hash:
                    # print(f'Can extend {head} to {head + 1}, ans = {ans + 1}')
                    ans += 1
                    head += 1
                    continue
                if tail - 1 in nums_hash:
                    # print(f'Can extend {tail} to {tail - 1}, ans = {ans + 1}')
                    ans += 1
                    tail -= 1
                    continue
                max_ans = max(ans, max_ans)
                # print(f"No head or tail found, breaking. Current ans = {ans}, max_ans = {max_ans}")
                break
            continue
        return max(ans, max_ans)