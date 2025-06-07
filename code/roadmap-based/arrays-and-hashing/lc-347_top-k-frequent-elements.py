from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Solution:
            We create a hashmap to count the occurrence of each unique
            number

            We then turn the keys and values into lists

            Then we can sort the value list, which is the count list,
            in max to min order and have it return the original list
            indices corresponding to the sorted order

            Then when we need to reference the top k most frequent, we
            just need to call first k elements in the sorted indices
            array and reference the key list, which are the unique nums

        Time Complexity: O(n) + O(n log(n))
            Constructing the hashmap will take O(n)

            Then sorted the keys can at most be O(n log(n))

        Space Complexity: O(n)
            We can at most have all unique numbers, which would then
            take up O(n) space when constructing the hashmap

        """
        count_dict = defaultdict(int)
        for n in nums:
            count_dict[n] += 1

        counts = list(count_dict.values())
        nums = list(count_dict.keys())

        sorted_indices = sorted(
            [i for i in range(len(counts))],
            key=lambda x: counts[x],
            reverse=True
        )

        ans = [nums[sorted_indices[i]] for i in range(k)]

        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [1,1,1,2,2,3]
    k = 2

    s.topKFrequent(nums, k)