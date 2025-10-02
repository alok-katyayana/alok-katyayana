"""
   Module for Min Heap Class
"""

class MinHeap:
    """
       Abstraction of Min Heap
    """
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * (index + 1)

    def _parent(self, index):
        return (index-1 )// 2

    def _swap(self, i1, i2):
        self.heap[i1], self.heap[i2] = self.heap[i2], self.heap[i1]

    def _trickle_up(self, index):
        while self._parent(index) >= 0 and self.heap[self._parent(index)] > self.heap[index]:
            self._swap(index, self._parent(index))
            index = self._parent(index)

    def _sink_down(self, index):
        min_index = index
        while True:
            l = self._left_child(index)
            r = self._right_child(index)

            if (l < len(self.heap)) and self.heap[l] < self.heap[min_index]:
                min_index = l
            if (r < len(self.heap)) and (self.heap[r] < self.heap[min_index]):
                min_index = r

            if min_index != index:
                self._swap(min_index, index)
                index = min_index

            else:
                return


    def remove(self):
        """
           Remove the top most element, Max value in this case.
        """
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop() 

        val = self.heap.pop(0)
        self.heap.insert(0, self.heap.pop())

        self._sink_down(0)

        return val


    def insert(self, value):
        """
           Insert a value into the heap.
        """
        self.heap.append(value)
        self._trickle_up(len(self.heap)-1)

    def print_heap(self):
        """
           Print the heap
        """
        print(self.heap)

if __name__ == "__main__":
    hp = MinHeap()

    hp.print_heap()

    hp.insert(99)
    hp.insert(72)
    hp.insert(61)
    hp.insert(58)
    hp.print_heap()
    hp.insert(100)
    hp.print_heap()


    hp.insert(75)
    hp.print_heap()

    hp.remove()
    hp.print_heap()

    myheap = MinHeap()
    myheap.insert(95)
    myheap.insert(75)
    myheap.insert(80)
    myheap.insert(55)
    myheap.insert(60)
    myheap.insert(50)
    myheap.insert(65)

    print(myheap.heap)


    myheap.remove()

    print(myheap.heap)


    myheap.remove()

    print(myheap.heap)
