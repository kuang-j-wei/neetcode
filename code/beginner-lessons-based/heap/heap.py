from typing import List

class MinHeap:
    def __init__(self):
        self.heap = [-1]

    def parent(self, idx) -> int:
        """
        Return the index of the parent node of the current node idx
        """
        return idx // 2

    def left_child(self, idx) -> int:
        """
        Return the index of the left child node of the current node idx
        """
        return 2 * idx

    def right_child(self, idx) -> int:
        """
        Return the index of the right child node of the current node idx
        """
        return 2 * idx + 1

    def top(self) -> int:
        """
        Return the value of the minimum number of the heap
        """
        return self.heap[1] if len(self.heap) > 1 else self.heap[0]

    def swap(self, curr, swp) -> None:
        """
        Swap the value of two elements, given their indices
        args:
            swp: int, the index of the node to be swapped in
            curr: int, the index of the node to be swapped
        """
        self.heap[curr], self.heap[swp] = self.heap[swp], self.heap[curr]

    def push(self, val) -> None:
        self.heap.append(val)

        # bubble up
        i = len(self.heap) - 1 # minus one because there is an additional 0

        while i > 1:  # so we terminate when root node is reached
            parent_idx = self.parent(i)
            if self.heap[parent_idx] > self.heap[i]:
                self.swap(i, parent_idx)
                i = parent_idx
            else:  # the right order has been achieved
                break

    def pop(self) -> int:
        if len(self.heap) == 1:
            return self.heap[0]
        elif len(self.heap) == 2:
            return self.heap.pop()

        root_val = self.heap[1]
        self.heap[1] = self.heap.pop()  # move last node to the top

        # bubble down, alway swap with the smallest child
        # continue to run until we don't have a left child or the two children
        # are already smaller
        self.percolate_down(1)
        return root_val
    
    def heapify(self, nums: List[int]) -> None:
        first_node_with_children = (len(nums) - 1) // 2
        self.heap = [-1] + nums[:]

        for i in range(first_node_with_children, 0, -1):
            self.percolate_down(i)
        return None

    def percolate_down(self, starting_index):
        i = starting_index
        n = len(self.heap)
        while True:
            left_index = self.left_child(i)
            right_index = self.right_child(i)
            if left_index < n:  # as long as a left child still exists, we not at bottom
                if (
                    right_index < n
                    and self.heap[right_index] < self.heap[left_index]
                    and self.heap[i] > self.heap[right_index]
                ):  # right exists, and right smaller, swap with right
                    self.swap(i, right_index)
                    i = right_index
                elif (
                    self.heap[i] > self.heap[left_index]
                ): # left smaller, swap with left
                    self.swap(i, left_index)
                    i = left_index
                else:  # current node already smaller than its children
                    break
            else:  # no left child, we are at the bottom
                break

if __name__ == "__main__":
    heap = MinHeap()
    heap.push(5)
    heap.push(2)
    heap.push(1)
    heap.push(10)

    assert heap.top() == 1
    assert heap.pop() == 1
    assert heap.top() == 2
    assert heap.pop() == 2
    assert heap.top() == 5
    assert heap.pop() == 5
    assert heap.top() == 10
    assert heap.pop() == 10
    heap.push(2)
    assert heap.pop() == 2

    nums = [1, 2, 3, 4, 5]
    heap.heapify(nums)
    assert heap.pop() == 1
    assert heap.pop() == 2
    assert heap.pop() == 3
    assert heap.pop() == 4
    assert heap.pop() == 5