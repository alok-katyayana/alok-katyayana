"""
   This Module Consists of class for Linked List
   and a helper Node class
"""

class Node:
    """ 
       This Class consists of each node in a Linked List.
       A node will have a pointer called next
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """
       This class is an abstraction for a Linked List. There is a pointer to the head
       and the rest of the list can be traversed from the head. There is also a Tail pointer for
       the end of the list.
    """

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """
           Print each value in the list, starting from the head!
        """
        temp = self.head
        while temp is not None:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("")

    def append(self, value):
        """
           Insert a new node into the list at the end.
        """
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

    def pop(self):
        """
           Removes and returns the last node from the list.
        """
        if self.head is None and self.tail is None:
            return False
        if self.head == self.tail:
            self.length -= 1
            node = self.head
            self.head = None
            self.tail = None
            return node
        tmp = self.head
        while tmp.next.next is not None:
            tmp = tmp.next
        self.tail = tmp
        node = tmp.next
        tmp.next = None
        self.length -= 1
        return node

    def prepend(self, value):
        """
           Insert a new node into the list at the beginning.
        """
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        """
           Removes and returns the first node from the list.
        """
        if self.head is None and self.tail is None:
            return False

        node = self.head

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = node.next
            node.next = None

        self.length -= 1
        return node

    def get(self,index):
        """
           Returns the value at a valid index, else returns None
        """
        print(f"Length of the list:{self.length}")
        if index < 0 or index >= self.length:
            return None
        tmp = self.head
        i = 0
        while tmp is not None:
            if index == i:
                break
            i += 1
            tmp = tmp.next
        return tmp


    def set_value(self, index, value):
        """
           Sets the value at a valid index, else returns False
        """
        print(f"Length of the list:{self.length}")
        node = self.get(index)

        if node:
            node.value = value
            return True
        return False

    def insert(self, index, value):
        """
           Inserts a new node with specified value at a valid index,
             else returns False
        """
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        pre_node = self.get(index - 1)
        post_node = self.get(index)

        new_node.next = post_node
        pre_node.next = new_node
        self.length += 1

        return True

    def remove(self, index):
        """
           Removes the node at a valid index,
             else returns None
        """
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        pre_node = self.get(index-1)
        node = pre_node.next
        pre_node.next = node.next
        node.next = None
        self.length -= 1
        return node

    def reverse(self ):
        """
           Reverses the whole list
        """
        if self.head is None:
            return False
        if self.head == self.tail:
            return True
        tmp = self.head
        self.head = self.tail
        self.tail = tmp

        before = None
        after = tmp.next
        while after is not None:
            after = tmp.next
            tmp.next = before 
            before = tmp
            tmp = after

        return True

    def inspect(self):
        """
        Inspect the list
        """
        print('head', end = " ")
        try:
            print(self.head, end=", ")
            print(f"Head Value:{self.head.value}")
        except AttributeError:
            print("Head is None")

        print("Head Next", end = " ")
        try:
            print(self.head.next, end=", ")
            print(f"Head Value:{self.head.next.value}")
        except AttributeError:
            print("Head Next is None")

        print("tail: ",end=" ")
        try:
            print(self.tail, end=", ")
            print(f"Tail Value:{self.tail.value}")
        except AttributeError:
            print("Tail is None")

        print("Tail Next: ", end = " ")
        try:
            print(self.tail.next, end=", ")
            print(f"Tail Value:{self.tail.next.value}", end=", ")
        except AttributeError:
            print("Tail Next is None")

        print(f"List Length: {self.length}")


if __name__ == "__main__":
    print("Append Test -------------------------------------------------------------------")
    my_ll = LinkedList(2)
    my_ll.append(4)
    my_ll.append(6)
    my_ll.append(8)
    my_ll.append(10)
    my_ll.append(12)
    my_ll.append(14)
    my_ll.print_list()
    my_ll.inspect()

    print("Remove Test -------------------------------------------------------------------")
    my_ll.remove(3)
    my_ll.print_list()
    my_ll.inspect()

    print("Insert Test -------------------------------------------------------------------")
    my_ll.insert(3,8)
    my_ll.print_list()
    my_ll.inspect()


    print("Reverse Test ------------------------------------------------------------------")
    my_ll.reverse()
    my_ll.print_list()
    my_ll.inspect()
