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

        res = self.heap[1]
        self.heap[1] = self.heap.pop()

        # bubble down
        # continue to run until we don't have a left child or the two children
        # are already smaller
        i = 1
        n = len(self.heap)
        while True:
            left = self.left_child(i)
            right = self.right_child(i)
            if left < n:  # as long as a left child still exists, we not at bottom
                if (
                    right < n
                    and self.heap[right] < self.heap[left]
                    and self.heap[i] > self.heap[right]
                ):  # swap with right
                    self.swap(i, right)
                    i = right
                elif (
                    right < n
                    and self.heap[left] < self.heap[right]
                    and self.heap[i] > self.heap[left]
                ): # swap with left
                    self.swap(i, left)
                    i = left
                else:  # current node already smaller than its children
                    break
            else:  # no left child, we are at the bottom
                break