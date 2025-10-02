"""
   This Module Implements Queue Data Structure.
"""


class Node:
    """
       Node in a Queue
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    """
       Abstraction for a Queue Data Structure
    """
    def __init__(self):
        self.next = None
        self.crowd = 0
        self.first = None
        self.last = None

    def print_queue(self):
        """
           Print the Queue
        """
        print(f"The crowd is {self.crowd}")
        tmp = self.first

        while tmp is not None:
            print(tmp.value, end="--")
            tmp = tmp.next

        print("\n")

    def enqueue(self, value):
        """
           Put an item into the queue
        """
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node

        else:
            self.last.next = new_node
            self.last = new_node

        self.crowd += 1
        return True

    def dequeue(self):
        """
           Remove an item from the queue
        """
        if self.first is None:
            return None

        tmp = self.first
        self.first = tmp.next

        tmp.next = None
        self.crowd -= 1
        return tmp


if __name__ == "__main__":
    q = Queue()

    q.print_queue()

    for i in range(5):
        q.enqueue(i)

    q.print_queue()

    try:
        for i in range(8):
            print(q.dequeue().value)
    except AttributeError as e:
        print(e)

    q.print_queue()
