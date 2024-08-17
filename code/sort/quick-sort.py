# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
    

class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs
    
    def quickSortHelper(self, pairs, start, end):
        if end - start <= 0:
            return pairs
        pivot_idx = end
        pivot = pairs[pivot_idx].key
        swap_pointer = start
        i = start

        while i <= pivot_idx:
            if pairs[i].key < pivot:
                temp = pairs[i]
                pairs[i] = pairs[swap_pointer]
                pairs[swap_pointer] = temp
                swap_pointer += 1
            i += 1
        temp = pairs[pivot_idx]
        pairs[pivot_idx] = pairs[swap_pointer]
        pairs[swap_pointer] = temp

        self.quickSortHelper(pairs, start, swap_pointer - 1)
        self.quickSortHelper(pairs, swap_pointer + 1, end)