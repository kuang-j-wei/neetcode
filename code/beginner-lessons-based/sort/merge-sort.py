from typing import List


class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
    def __repr__(self) -> str:
        return f'({self.key}, "{self.value}")'


class SolutionUnOptimized:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        """
        The space complexity here is O(n log(n)), which is not good
        
        This is because we have log(n) recursive stack

        But in each level, we have to create a new array, which cost n

        So total space is n * log(n)
        """
        if len(pairs) <= 1:
            return pairs


        mid = len(pairs) // 2
        end = len(pairs)
        
        left_list = self.mergeSort(pairs[:mid])
        right_list = self.mergeSort(pairs[mid:end])
        pairs = self.merge(left_list, right_list)

        return pairs
    
    def merge(self, l1, l2):
        array = [None] * (len(l1) + len(l2))
        l1_idx = 0
        l2_idx = 0
        idx = 0
        
        while l1_idx < len(l1) and l2_idx < len(l2):
            if l1[l1_idx].key <= l2[l2_idx].key:
                array[idx] = l1[l1_idx]
                l1_idx += 1
            else:
                array[idx] = l2[l2_idx]
                l2_idx += 1
            idx += 1
        
        array[idx:] = l2[l2_idx:] if l1_idx == len(l1) else l1[l1_idx:]
        return array


class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        """
        Time complexity is O(n * log(n)) because there the depth is log(n),
        and each depth we have to at most do n computation to compare size

        Space complexity is O(log(n) + n) because there are log(n) call stacks,
        and we also have to at most create n sub-copies when making the merge
        step
        """
        return self.mergeSortInPlace(pairs, 0, len(pairs))

    def mergeSortInPlace(self, array, start, end):
        if end - start <= 1:
            return array

        mid = ((end - start) // 2) + start

        self.mergeSortInPlace(array, start, mid)
        self.mergeSortInPlace(array, mid, end)
        self.merge(array, start, mid, end)
        
        return array

    def merge(self, array, start, mid, end):
        left_array = array[start:mid]
        right_array = array[mid:end]
        left_idx = 0
        right_idx = 0
        
        while left_idx < len(left_array) and right_idx < len(right_array):
            if left_array[left_idx].key <= right_array[right_idx].key:
                array[start] = left_array[left_idx]
                left_idx += 1
            else:
                array[start] = right_array[right_idx]
                right_idx += 1
            start += 1
        
        array[start:end] = left_array[left_idx:] if right_idx >= len(right_array) else right_array[right_idx:]
        return array


def mergeDebug(array, start, mid, end):
    i, j, k = start, 0, 0
    
    left_array = array[start:(mid + 1)]
    right_array = array[(mid + 1):(end + 1)]
    print(f"left_array = {left_array}")
    print(f"right_array = {right_array}")
    
    while i <= end:
        print(f"(i, j, k) = ({i}, {j}, {k})")
        if left_array[j] <= right_array[k]:
            array[i] = left_array[j]
            j += 1
            if j >= len(left_array):
                array[i+1:end+1] = right_array[k:len(right_array) + 1]
                break
        else:
            array[i] = right_array[k]
            k += 1
            if k >= len(right_array):
                array[i+1:end+1] = left_array[j:len(left_array) + 1]
                break
        i += 1
    print(f"Exiting merge() with current array = {array}")
    return array


def mergeSortDebug(array, start, end):
    if end - start + 1 <= 1:
        return array
    
    mid = (start + end) // 2
    print(f"Calling mergeSort({array}, {start}, {mid})")
    mergeSortDebug(array, start, mid)
    print(f"Calling mergeSort({array}, {mid + 1}, {end})")
    mergeSortDebug(array, mid + 1, end)
    print(f"Calling merge({array}, {start}, {mid}, {end})")
    mergeDebug(array, start, mid, end)
    return array



if __name__ == '__main__':
    DEBUG = False
    array = [3, 2, 4, 1, 6]
    array_copied = array.copy()
    if DEBUG:
        sorted_array = mergeSortDebug(array, 0, len(array) - 1)
        array.sort()
        assert array == sorted_array, "Failed"
        print(f"\nOriginal array = {array_copied}")
        print(f"Sorted array = {sorted_array}")
    else:
        s = Solution()
        input = [
            Pair(5, "apple"),
            Pair(2, "banana"),
            Pair(9, "cherry"),
            Pair(1, "date"),
            Pair(9, "elderberry")
        ]
        sorted_list = s.mergeSort(input)
        print(f"Input list: {input}")
        print(f"Sorted list: {sorted_list}")