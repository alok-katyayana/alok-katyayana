"""
   Exercises related to Doubly Linked List 
"""

from doubly_linked_list import Node, DoublyLinkedList

## Palindrome Checker

def is_palindrome(dll:DoublyLinkedList) -> bool:
    """
       Return True if the list is a palindrome else, return False
    """
    forwd = dll.head
    bcrwd = dll.tail
    is_pal = True
    con_check_for = lambda nd : (nd is not None and nd.next is not None)
    con_check_bck = lambda nd : (nd is not None and nd.prev is not None)
    while con_check_for(forwd) and con_check_bck(bcrwd):
        if forwd.value != bcrwd.value:
            is_pal = False
            return is_pal
        if forwd == bcrwd:
            return is_pal

        forwd = forwd.next
        bcrwd = bcrwd.prev

    return is_pal

def reverse(dll: DoublyLinkedList) -> DoublyLinkedList:
    """
       Returns the reverse of the list
    """
    tmp = dll.head

    while tmp is not None:
        cur = tmp.next
        tmp.next = tmp.prev
        tmp.prev = cur

        tmp = cur

    t1 = dll.head
    dll.head = dll.tail

    dll.tail = t1

    return dll

def partition_list(dll: DoublyLinkedList, x: int) -> DoublyLinkedList:
    """
       Rearrange the list so that all values below x are towards one side
       and values greater than x are on another side. 
    """
    d1 = Node("dum1")
    d2 = Node("dum2")

    p1 = d1
    p2 = d2

    tmp = dll.head

    if dll.head is None or (dll.length == 1):
        return dll

    while tmp is not None:
        if tmp.value < x:
            p1.next = tmp
            tmp.prev = p1
            p1 = p1.next

        elif tmp.value >= x:
            p2.next = tmp
            tmp.prev = p2
            p2 = p2.next

        tmp = tmp.next

    p2.next = None
    p1.next = d2.next
    if d2.next is not None:
        d2.next.prev = p1

    dll.head = d1.next
    dll.head.prev = None
    dll.tail = p2

    p1 = None
    p2 = None
    d1 = None
    d2 = None
    return dll


def reverse_between(dll: DoublyLinkedList, start: int, end: int) -> DoublyLinkedList:
    """
       Returns a new list where elements are revered between to specific indexes.
    """
    if (start < 0) or (end >= dll.length):
        return dll

    if start >= end:
        return dll

    d = Node("dumdum")
    d.next = dll.head

    pre = d
    for _ in range(start):
        pre = pre.next

    cur = pre.next

    for _ in range(end-start):
        tm = cur.next
        cur.next = tm.next
        if tm.next:
            tm.next.prev = cur
        tm.next = pre.next
        pre.next.prev = tm
        tm.prev = pre
        pre.next = tm

    dll.head = d.next
    d = None

    dll.head.prev = None

    return dll

def swap_pairs(dll):
    """
       Swap values in the consecutive pairs
    """
    if dll.head is None:
        return None

    if dll.head == dll.tail:
        return dll

    dum = Node("dumdum")
    dum.next = dll.head

    pre = dum
    first = dum.next
    second = first.next

    nexti = second.next

    while True:
        try:
            pre.next = second
            second.prev = pre

            second.next = first
            first.prev = second
            first.next = nexti

            pre = first
            first = pre.next
            second = first.next
            nexti = second.next
        except AttributeError:
            break

    dll.head = dum.next

    dll.head.prev = None
    return dll


if __name__ == "__main__":
    print("---------------Testing Palindrome Exercise-------------")

    my_dll_1 = DoublyLinkedList(1)
    my_dll_1.append(2); my_dll_1.append(3); my_dll_1.append(3); my_dll_1.append(2); my_dll_1.append(1)

    print('my_dll_1 is_palindrome:')
    print(is_palindrome(my_dll_1))


    my_dll_2 = DoublyLinkedList(1)
    my_dll_2.append(2)
    my_dll_2.append(3)

    print('\nmy_dll_2 is_palindrome:')
    print( is_palindrome(my_dll_2) )



    print("---------------Testing Palindrome Exercise-------------")
    my_dll_1.append(10); my_dll_1.append(11);my_dll_1.append(12);
    my_dll_1.print_list()
    rev = reverse(my_dll_1)
    rev.print_list()

    print("---------------Testing Partition Exercise-------------")
    rev.print_list()
    new_rev = partition_list(rev,6)
    new_rev.print_list()

    print("\nTest Case 1: Partition around 5")
    dll1 = DoublyLinkedList(3)
    dll1.append(8)
    dll1.append(5)
    dll1.append(10)
    dll1.append(2)
    dll1.append(1)
    print("BEFORE: ", end="")
    dll1.print_list()
    dll1 = partition_list(dll1, 5)
    print("AFTER:  ", end="")
    dll1.print_list()

    print("\nTest Case 2: All nodes less than x")
    dll2 = DoublyLinkedList(1)
    dll2.append(2)
    dll2.append(3)
    print("BEFORE: ", end="")
    dll2 = partition_list(dll2, 5)
    dll2.print_list()
    print("AFTER:  ", end="")
    dll2.print_list()

    print("\nTest Case 3: All nodes greater than x")
    dll3 = DoublyLinkedList(6)
    dll3.append(7)
    dll3.append(8)
    print("BEFORE: ", end="")
    dll3.print_list()
    dll3 = partition_list(dll3, 5)
    print("AFTER:  ", end="")
    dll3.print_list()

    print("\nTest Case 4: Empty list")
    dll4 = DoublyLinkedList(1)
    dll4.make_empty()
    print("BEFORE: ", end="")
    dll4.print_list()
    dll4 = partition_list(dll4, 5)
    print("AFTER:  ", end="")
    dll4.print_list()

    print("\nTest Case 5: Single node")
    dll5 = DoublyLinkedList(1)
    print("BEFORE: ", end="")
    dll5.print_list()
    dll5 = partition_list(dll5, 5)
    print("AFTER:  ", end="")
    dll5.print_list()

    print("\nTesting Reverse between")
    dll1.print_list()
    dll6 = reverse_between(dll1, 0, 5)
    dll6.print_list()


    print("\n Testing Swap")

    dll1 = DoublyLinkedList(3)
    dll1.append(8)
    dll1.append(5)
    dll1.append(10)
    dll1.append(2)
    dll1.append(1)
    dll1.print_list()
    new_dll = swap_pairs(dll1)
    new_dll.print_list()
