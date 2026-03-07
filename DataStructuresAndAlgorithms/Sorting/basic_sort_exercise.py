## Bubble Sort on LL

from linkedlist import LinkedList, Node

def _swap(n1:Node, n2:Node):
        n1.value, n2.value = n2.value, n1.value


def bubble_sort(lst: LinkedList):
    for i in range(lst.length):
        tmp = lst.head
        while tmp is not None and tmp.next is not None:
            if tmp.value > tmp.next.value:
                _swap(tmp, tmp.next)

            tmp = tmp.next

    return lst

def selection_sort(lst: LinkedList):
    min_n = lst.head

    while min_n is not None and min_n.next is not None:
        tmp = min_n.next
        while tmp is not None:
            if min_n.value > tmp.value:
                _swap(min_n, tmp)
            tmp = tmp.next

        min_n = min_n.next

    return lst

def insertion_sort(lst: LinkedList):
    if lst.length < 2:
        return
    
    sorted_list_head = lst.head
    unsorted_list_head = lst.head.next
    sorted_list_head.next = None
    
    while unsorted_list_head is not None:
        current = unsorted_list_head
        unsorted_list_head = unsorted_list_head.next
        
        if current.value < sorted_list_head.value:
            current.next = sorted_list_head
            sorted_list_head = current
        else:
            search_pointer = sorted_list_head
            while search_pointer.next is not None and current.value > search_pointer.next.value:
                search_pointer = search_pointer.next
            current.next = search_pointer.next
            search_pointer.next = current

    lst.head = sorted_list_head
    temp = lst.head
    while temp.next is not None:
        temp = temp.next
    lst.tail = temp

    return lst



if __name__ == "__main__":
    my_linked_list = LinkedList(4)
    my_linked_list.append(2)
    my_linked_list.append(6)
    my_linked_list.append(5)
    my_linked_list.append(1)
    my_linked_list.append(3)
    
    print("Linked List Before Sort:")
    my_linked_list.print_list()
    
    my_linked_list_s = bubble_sort(my_linked_list)
    
    print("\nSorted Linked List:")
    my_linked_list_s.print_list()

    print("\nTesting Selection Sort")
    # Test Cases:
    # -----------------------------------
    
    # Test 1: Empty list
    print("Test 1: Empty list")
    ll1 = LinkedList(5)
    ll1.head = None
    ll1.length = 0
    selection_sort(ll1)
    ll1.print_list()  # Should print: empty
    print("-" * 30)
    
    # Test 2: Single element
    print("Test 2: Single element")
    ll2 = LinkedList(5)
    selection_sort(ll2)
    ll2.print_list()  # Should print: 5
    print("-" * 30)
    
    # Test 3: Already sorted list
    print("Test 3: Already sorted list")
    ll3 = LinkedList(1)
    ll3.append(2)
    ll3.append(3)
    selection_sort(ll3)
    ll3.print_list()  # Should print: 1 -> 2 -> 3
    print("-" * 30)
    
    # Test 4: Reverse order
    print("Test 4: Reverse order")
    ll4 = LinkedList(3)
    ll4.append(2)
    ll4.append(1)
    selection_sort(ll4)
    ll4.print_list()  # Should print: 1 -> 2 -> 3
    print("-" * 30)
    
    # Test 5: Random order
    print("Test 5: Random order")
    ll5 = LinkedList(2)
    ll5.append(1)
    ll5.append(3)
    selection_sort(ll5)
    ll5.print_list()  # Should print: 1 -> 2 -> 3
    print("-" * 30)
    
    # Test 6: List with duplicates
    print("Test 6: List with duplicates")
    ll6 = LinkedList(3)
    ll6.append(2)
    ll6.append(2)
    ll6.append(1)
    ll6.append(3)
    selection_sort(ll6)
    ll6.print_list()  # Should print: 1 -> 2 -> 2 -> 3 -> 3
    print("-" * 30)
    
     
    print("\nTesting Insertion Sort")
    # Test Cases:
    # -----------------------------------
    
    # Test 1: Empty list
    print("Test 1: Empty list")
    ll1 = LinkedList(5)
    ll1.head = None
    ll1.length = 0
    insertion_sort(ll1)
    ll1.print_list()  # Should print: empty
    print("-" * 30)
    
    # Test 2: Single element
    print("Test 2: Single element")
    ll2 = LinkedList(5)
    insertion_sort(ll2)
    ll2.print_list()  # Should print: 5
    print("-" * 30)
    
    # Test 3: Already sorted list
    print("Test 3: Already sorted list")
    ll3 = LinkedList(1)
    ll3.append(2)
    ll3.append(3)
    insertion_sort(ll3)
    ll3.print_list()  # Should print: 1 -> 2 -> 3
    print("-" * 30)
    
    # Test 4: Reverse order
    print("Test 4: Reverse order")
    ll4 = LinkedList(3)
    ll4.append(2)
    ll4.append(1)
    insertion_sort(ll4)
    ll4.print_list()  # Should print: 1 -> 2 -> 3
    print("-" * 30)
    
    # Test 5: Random order
    print("Test 5: Random order")
    ll5 = LinkedList(2)
    ll5.append(1)
    ll5.append(3)
    insertion_sort(ll5)
    ll5.print_list()  # Should print: 1 -> 2 -> 3
    print("-" * 30)
    
    # Test 6: List with duplicates
    print("Test 6: List with duplicates")
    ll6 = LinkedList(3)
    ll6.append(2)
    ll6.append(2)
    ll6.append(1)
    ll6.append(3)
    insertion_sort(ll6)
    ll6.print_list()  # Should print: 1 -> 2 -> 2 -> 3 -> 3
    print("-" * 30)
    
    
