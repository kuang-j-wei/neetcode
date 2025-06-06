# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
    def __repr__(self) -> str:
        return f'({self.key}, "{self.value}")'

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        output = []
        
        for i in range(len(pairs)):
            for j in range(i - 1, -1, -1):
                prev_pair = pairs[j]
                curr_pair = pairs[j + 1]

                if prev_pair.key > curr_pair.key:
                    pairs[j] = curr_pair
                    pairs[j + 1] = prev_pair
                else:
                    break
            output.append(pairs.copy())  # otherwise we are just pointing to the array that continuously get modified, instead of having a history of the changes
        return output



pairs = [Pair(5, 'apple'), Pair(2, 'banana'), Pair(9, 'cherry')]
output = insertionSort(pairs)
print(output)