"""
   This Module Consists of class for Doubly Linked List
   and a helper Node class
"""
class Node:
    """ 
       This Class consists of each node in a Doubly Linked List.
       A node will have two pointers called next and prev
    """
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None



class DoublyLinkedList():
    """
       This class is an abstraction for a Doubly Linked List. There is a pointer to the head
       and the rest of the list can be traversed from the head. There is also a Tail pointer for
       the end of the list.
    """

    def __init__(self, value):
        nn = Node(value)
        self.head = nn
        self.tail = nn
        self.length = 1

    def print_list(self):
        """
           Print each value in the list, starting from the head!
        """
        print(f"The number of elements in the list is: {self.length}")
        temp = self.head
        while temp is not None:
            print(f"<- {temp.value}", end=" -> ")
            temp = temp.next
        print("")

    def append(self, value):
        """
           Insert a new node into the list at the end.
        """
        nn = Node(value)
        if self.head is None:
            self.head = nn
            self.tail = nn
        else:
            self.tail.next = nn
            nn.prev = self.tail
            self.tail = nn

        self.length += 1

        return True

    def pop(self):
        """
           Removes and returns the last node from the list.
        """
        if self.head is None:
            return None

        tmp = self.tail
        if self.head == self.tail:
            self.head = None
            self.tail = None

        else:
            self.tail = self.tail.prev
            tmp.prev = None
            self.tail.next = None

        self.length -= 1

        return tmp

    def prepend(self, value):
        """
           Insert a new node into the list at the beginning.
        """
        nn = Node(value)
        if self.head is None:
            res = self.append(value)
        else:
            nn.next = self.head
            self.head.prev = nn 
            self.head = nn
            res = True
            self.length += 1
        return res

    def pop_first(self):
        """
           Removes and returns the first node from the list.
        """
        if self.head is None:
            return None

        if self.head == self.tail:
            res = self.pop()

        else:
            res = self.head
            self.head = self.head.next
            self.head.prev = None
            res.next = None
            self.length -= 1

        return res

    def get(self, index):
        """
           Returns the value at a valid index, else returns None
        """
        if index < 0 or index >= self.length:
            return None

        tmp = self.head
        for _ in range(index):
            tmp = tmp.next

        return tmp

    def set_value(self, index, value):
        """
           Sets the value at a valid index, else returns False
        """
        nd = self.get(index)

        if nd is None:
            return False

        nd.value = value
        return True

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

        nn = Node(value)
        before = self.get(index)
        after = before.next
        nn.prev = before
        nn.next = after

        before.next = nn
        after.prev = nn
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

        if index == self.length-1:
            return self.pop()

        res = self.get(index)

        res.prev.next = res.next
        res.next.prev = res.prev

        res.prev = None
        res.next = None

        self.length -= 1

        return res


    def make_empty(self):
        """
           Removes all the nodes from the list
        """
        self.head = None
        self.tail = None
        self.length = 0


if __name__ == "__main__":
    print("----------Test DLL Construct----------")
    edl = DoublyLinkedList(88888888)
    edl.print_list()

    print("----------Test Append----------")
    edl.append(100)
    edl.append(103)
    edl.append(10)
    edl.print_list()

    print("----------Test pop----------")
    i = edl.pop()
    while i is not None:
        print(f"Popped Value is {i.value}")
        edl.print_list()
        i = edl.pop()



    print("----------Test Prepend----------")
    for i in range(100, 106):
        edl.prepend(i)
        edl.print_list()

    print("----------Test Pop First----------")
    i = edl.pop_first()
    while i is not None:
        print(f"Popped Value is {i.value}")
        edl.print_list()
        i = edl.pop()


    print("----------Test get----------")
    for i in range(105,1100,100):
        edl.prepend(i)
        edl.append(i**2)

    edl.print_list()
    for i in range(10):
        print("index: ",i)
        print(edl.get(i).value)

    print("----------Test Set----------")
    edl.print_list()
    for i in range(-10,10,2):
        RES = edl.set_value(i, i*10)
        print(RES)

    edl.print_list()

    print("----------Test Insert Method----------")
    edl.print_list()
    test_index = [-10,0,5,20,21,229]
    for elm in test_index:
        print(edl.insert(elm, id(elm)))
        print(elm)

    edl.print_list()

    print("----------Test Remove Method----------")
    for i in range(0, edl.length, 2):
        edl.pop()
    edl.print_list()
    test_index = [-10,0,1,2,8,7,9,21,229]
    for elm in test_index:
        print(elm)
        print(edl.remove(elm))

    edl.print_list()
