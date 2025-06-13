from typing import List
from collections import defaultdict
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Solution:
            We first count the number of occurrence of each unique
            number

            Then we construct another array where the index represents
            how many times a number appears

            This array is guaranteed to be at most of size n because
            that would only happen if each element in nums is unique
            
            Since we already used a hashmap to count the occurrence, we
            can just loop through the keys and directly index the count
            array

            Then in the count array, we can make each element a list,
            and we can then just append the list with the unique number

            Finally, to get k top frequent elements, we can iterate from
            the back of that count array, until we've accumulated enough
            unique numbers (the question states we are guaranteed to
            have an unique solution so we don't have to worry about
            the output array actually exceeding size k)

        Time Complexity: O(n)
            We do an O(n) pass for 3 times

        Space Complexity: O(n)
            We need count_dict and frequency each can take up to O(n)
        """
        length = len(nums)
        count_dict = {}
        frequency = [[] for i in range(length + 1)]
        ans = []

        for n in nums:
            count_dict[n] = 1 + count_dict.get(n, 0)
        
        for n, count in count_dict.items():
            frequency[count].append(n)

        idx = length
        while len(ans) < k:
            ans.extend(frequency[idx])
            idx -= 1

        return ans


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Solution:
            We first count the occurrence of numbers using a hashmap.
            
            Then we construct a min heap, using the count as the sorting
            key. When the heap is bigger than k, we know we need to
            start kicking elements out. And since this is a min heap, if
            we always kick out the smallest count number, then we know
            at the end we will have the k biggest numbers left in the
            heap

            We can then just loop through the heap and collect the
            unique numbers as our solution



        Time Complexity: O(n log(k))
            Because heappush can take log(k), and we have to do this n
            times when we are constructing the min_heap
        
        Space Complexity: O(n + k) total space
            O(n) because we still need to construct the count dict which
            could at most be O(n)

            Min heap will be of size O(k)
        """
        length = len(nums)
        count_dict = {}
        min_heap = []
        ans = []

        for n in nums:
            count_dict[n] = 1 + count_dict.get(n, 0)
        
        for n, count in count_dict.items():
            heapq.heappush(min_heap, (count, n))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        for _ in range(k):
            count, n = heapq.heappop(min_heap)
            ans.append(n)
        return ans


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