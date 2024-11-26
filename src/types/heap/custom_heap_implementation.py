class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    # this function makes sure that the heap property is maintained
    # parent node is smaller than or equal to its children
    def heapify_down(self, index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            # swap the index and smallest element's index
            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index],
            )
            self.heapify_down(smallest)

    def heapify_up(self, index):
        while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.heap[index], self.heap[self.parent(index)] = (
                self.heap[self.parent(index)],
                self.heap[index],
            )
            index = self.parent(index)

    def insert(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root

    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def __str__(self):
        return str(self.heap)


#############
class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    # Ensures that the heap property is maintained
    # Parent node is larger than or equal to its children
    def heapify_down(self, index):
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            # Swap the index and the largest element's index
            self.heap[index], self.heap[largest] = (
                self.heap[largest],
                self.heap[index],
            )
            self.heapify_down(largest)

    def heapify_up(self, index):
        # While the node's parent is smaller than the node itself
        while index > 0 and self.heap[self.parent(index)] < self.heap[index]:
            self.heap[index], self.heap[self.parent(index)] = (
                self.heap[self.parent(index)],
                self.heap[index],
            )
            index = self.parent(index)

    def insert(self, key):
        # Insert the new key at the end and move it up to restore heap property
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        # Replace the root with the last element and restore heap property
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root

    def peek(self):
        # Return the maximum element (the root of the heap)
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def __str__(self):
        return str(self.heap)
