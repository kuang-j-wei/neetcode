class MinHeap:
    def __init__(self):
        self.heap = [0]

    def parent(self, idx):
        return idx // 2

    def left_child(self, idx):
        return 2 * idx

    def right_child(self, idx):
        return 2 * idx + 1

    def min(self):
        return self.heap[1]

    def swap(self, curr, swp):
        """
        args:
            swp: int, the index of the node to be swapped in
            curr: int, the index of the node to be swapped
        """
        self.heap[curr], self.heap[swp] = self.heap[swp], self.heap[curr]

    def push(self, val):
        self.heap.append(val)

        # bubble up
        i = len(self.heap) - 1 # minus one because there is an additional 0

        while i > 1:  # so we terminate when root node is reached
            if self.heap[self.parent(i)] > self.heap[i]:
                self.swap(i, self.parent(i))
                i = self.parent(i)
            else:  # the right order has been achieved
                break

    def pop(self):
        if len(self.heap) == 1:
            return None
        elif len(self.heap) == 2:
            return self.heap.pop()

        root_idx = self.heap[1]
        self.heap[1] = self.heap.pop()  # move last node to the top

        # bubble down, alway swap with the smallest child
        # continue to run until we don't have a left child or the two children
        # are already smaller
        i = 1
        n = len(self.heap)
        while True:
            left_index = self.left_child(i)
            right_index = self.right_child(i)
            if left_index < n:  # as long as a left child still exists, we not at bottom
                if (
                    right_index < n
                    and self.heap[right_index] < self.heap[left_index]
                    and self.heap[i] > self.heap[right_index]
                ):  # swap with right
                    self.swap(i, right_index)
                    i = right_index
                elif (
                    right_index < n
                    and self.heap[left_index] < self.heap[right_index]
                    and self.heap[i] > self.heap[left_index]
                ): # swap with left
                    self.swap(i, left_index)
                    i = left_index
                else:  # current node already smaller than its children
                    break
            else:  # no left child, we are at the bottom
                break
        return root_idx

if __name__ == "__main__":
    heap = MinHeap()
    heap.push(10)
    heap.push(4)
    heap.push(15)
    heap.push(20)
    heap.push(1)

    assert heap.min() == 1
    assert heap.pop() == 1
    assert heap.min() == 4
    heap.push(2)
    assert heap.pop() == 2
