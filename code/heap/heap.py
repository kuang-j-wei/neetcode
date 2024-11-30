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

        while i > 1:
            if self.heap[self.parent(i)] > self.heap[i]:
                tmp = self.parent(i)
                self.heap[self.parent(i)] = self.heap[i]
                self.heap[i] = tmp
                i = self.parent(i)
            else:
                break